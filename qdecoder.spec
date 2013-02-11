Summary:	CGI library for C/C++ language
Name:		qdecoder
Version:	11.0.0
Release:	2
Epoch:		11
License:	GPL
Group:		Development/C
URL:		http://www.qdecoder.org
Source0:	ftp://ftp.qdecoder.org/pub/qDecoder/qDecoder-%{version}.tar.gz
BuildRequires:	%{_lib}mysql-devel

%description
qDecoder is a development kit for C/C++ programming language. It was developed
for the needs of building well formed CGI library at the beginning. But now it
covers most of general topics we may face while we develop softwares.
For example, qDecoder covers following areas.

    * Data Structures - Hash table(dynamic & static), Linked-list,
      Queue(Stack & FIFO), Obstack, ...
    * En/decoders and Hashes API - Base64 encoding, URL encoding,
      MD5 hash, FNV32 hash, ...
    * Network & IPC interfacing API - HTTP client, Timeout I/O,
      Shared memory API, Semaphore API, ...
    * CGI/FastCGI API - CGI request parser & response generator,
      CGI session controll, FastCGI, ...
    * Database Wrapper API - MySQL, ...
    * Specialized features - General configuration file parser,
      Rotating file logger, Server side includes, ...
    * General topics - String APIs, File APIs, ...

%package devel
Summary:	Devel package to qDecoder
Group:		Development/C
Requires:	qdecoder >= %{epoch}:%{version}

%description devel
Devel package to qDecoder

%package examples
Summary:	Examples to qDecoder
Group:		Development/C
Requires:	qdecoder >= %{epoch}:%{version}

%description examples
Example files to qDecoder

%prep
%setup -q -n qDecoder-%{version}

%build
%configure2_5x \
	--enable-mysql=%{_includedir}/mysql

%make

pushd examples
	%make
popd

%install
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}
%makeinstall LIBDIR=%{buildroot}%{_libdir} HEADERDIR=%{buildroot}%{_includedir}
install -d %{buildroot}%{_datadir}/%{name}
cp examples/*.{cgi,html,c} %{buildroot}%{_datadir}/%{name}
#cp -r examples/qDecoder-upload %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_webappconfdir}
cat > %{buildroot}%{_webappconfdir}/%{name}.conf <<EOF
Alias /%{name} %{_datadir}/%{name}
<Directory %{_datadir}/%{name}>
    Order deny,allow
    Deny from all
    Allow from 127.0.0.1
    ErrorDocument 403 "Access denied per %{_webappconfdir}/%{name}.conf"
</Directory>
EOF

%clean

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libqdecoder.so.%{epoch}
%{_libdir}/libqdecoder.so

%files devel
%defattr(-,root,root)
%doc examples doc/html
%{_libdir}/libqdecoder.a
%{_includedir}/qdecoder.h

%files examples
%defattr(-,root,root)
%doc examples/*.c
%config(noreplace) %{_webappconfdir}/%{name}.conf
%{_datadir}/%{name}


%changelog
* Mon Feb 28 2011 Lonyai Gergely <aleph@mandriva.org> 11:11.0.0-1mdv2011.0
+ Revision: 641055
- 11.0.0

* Thu Nov 11 2010 Lonyai Gergely <aleph@mandriva.org> 8:10.1.6-1mdv2011.0
+ Revision: 595944
- 10.1.6

* Thu Apr 22 2010 Lonyai Gergely <aleph@mandriva.org> 8:10.1.2-3mdv2010.1
+ Revision: 537798
- ILENT: bump
- Mv examples to a separated package
- Fix: the group in devel package
- 10.1.2
  initial version
- create qdecoder

