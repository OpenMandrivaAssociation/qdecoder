Summary:	CGI library for C/C++ language
Name:		qdecoder
Version:	10.1.2
Release:	%mkrel 2
Epoch:		8
License:	GPL
Group:		Development/C
URL:		http://www.qdecoder.org
Source0:	ftp://ftp.qdecoder.org/pub/qDecoder/qDecoder-%{version}.tar.gz
BuildRequires:	%{_lib}mysql-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
qDecoder is a development kit for C/C++ programming language. It was developed for the needs of building well formed CGI library at the beginning. But now it covers most of general topics we may face while we develop softwares.
For example, qDecoder covers following areas.

    * Data Structures - Hash table(dynamic & static), Linked-list, Queue(Stack & FIFO), Obstack, ...
    * En/decoders and Hashes API - Base64 encoding, URL encoding, MD5 hash, FNV32 hash, ...
    * Network & IPC interfacing API - HTTP client, Timeout I/O, Shared memory API, Semaphore API, ...
    * CGI/FastCGI API - CGI request parser & response generator, CGI session controll, FastCGI, ...
    * Database Wrapper API - MySQL, ...
    * Specialized features - General configuration file parser, Rotating file logger, Server side includes, ...
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
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}
%makeinstall LIBDIR=%{buildroot}%{_libdir} HEADERDIR=%{buildroot}%{_includedir}
install -d %{buildroot}%{_datadir}/%{name}
cp examples/*.{cgi,conf,html,in} %{buildroot}%{_datadir}/%{name}
cp -r examples/qDecoder-upload %{buildroot}%{_datadir}/%{name}
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
rm -rf %{buildroot}

%post examples
%if %mdkversion < 201010
%_post_webapp
%endif

%postun examples
%if %mdkversion < 201010
%_postun_webapp
%endif

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES COPYING
%{_libdir}/libqDecoder.so.%{epoch}
%{_libdir}/libqDecoder.so

%files devel
%defattr(-,root,root)
%doc examples doc/html
%{_libdir}/libqDecoder.a
%{_includedir}/qDecoder.h

%files examples
%defattr(-,root,root)
%doc examples/*.c
%config(noreplace) %{_webappconfdir}/%{name}.conf
%{_datadir}/%{name}
