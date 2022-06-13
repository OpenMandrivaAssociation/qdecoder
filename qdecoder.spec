%define major 12
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	CGI library for C/C++ language
Name:		qdecoder
Version:	12.1.0
Release:	1
Epoch:		11
License:	BSD
Group:		Development/C
Url:		http://www.qdecoder.org
Source0:	https://github.com/wolkykim/qdecoder/archive/%{name}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc

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

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Development files for qDecoder
Group:		Development/C
Conflicts:	%{name} < 11:12.0.5
Obsoletes:	%{name} < 11:12.0.5

%description -n %{libname}
Development files for qDecoder.

%files -n %{libname}
%{_libdir}/libqdecoder.so.%{major}

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for qDecoder
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name} < 11:12.0.5
Obsoletes:	%{name}-devel < 11:12.0.5

%description -n %{devname}
Development files for qDecoder.

%files -n %{devname}
%doc doc/html COPYING
%{_libdir}/libqdecoder.so
%{_libdir}/libqdecoder.a
%{_includedir}/qdecoder.h
%{_libdir}/pkgconfig/qdecoder.pc

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
export CC=gcc
export CXX=g++
%configure
%make_build

%install
%make_install
