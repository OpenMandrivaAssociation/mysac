%define major 0.0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Provides mechanisms for making asynchronous request to MySQL database
Name:		mysac
Version:	1.1.1
Release:	4
License:	GPLv2+
Group:		Networking/Other
Url:		http://www.arpalert.org/mysac.html
Source0:	http://www.arpalert.org/src/%{name}-%{version}.tar.gz
Patch0:		mysac-makefile.patch
BuildRequires:	mysql-devel

%description
MySAC is a library that provides mechanisms for making asynchronous
request to MySQL database. It uses uses the official MySQL client
library for authentication and network functions. Memory allocation
must be done in user code, so any memory manager can be used.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for mysac
Group:		System/Libraries
Conflicts:	%{_lib}mysac0 < 1.1.1-3
Obsoletes:	%{_lib}mysac0 < 1.1.1-3

%description -n %{libname}
MySAC is a library that provides mechanisms for making asynchronous
request to MySQL database. It uses uses the official MySQL client
library for authentication and network functions. Memory allocation
must be done in user code, so any memory manager can be used.

%files -n %{libname}
%{_libdir}/libmysac.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the mysac library
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for the mysac library.

%files  -n %{devname}
%{_includedir}/*.h
%{_libdir}/libmysac.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .makefile

%build
%make \
	CFLAGS="%{optflags} -DBUILDVER=%{version} -I/usr/include/mysql " \
	LDFLAGS="%{ldflags} -lmysqlclient_r"

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
install -m0755 libmysac.so.%{major} %{buildroot}%{_libdir}
install -m0755 *.h  %{buildroot}%{_includedir}
pushd %{buildroot}%{_libdir}
ln -s libmysac.so.%{major} libmysac.so
popd
