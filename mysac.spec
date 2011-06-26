%define name    mysac
%define version 1.1.1
%define release %mkrel 1
%define major 0
%define libname %mklibname %{name}  %{major}
%define develname %mklibname %{name} -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    	MySACL library: MySAC is a library that provides mechanisms for making asynchronous request to MySQL database.
License:    	GPLv3+
Group:      	Networking/Other
URL:        	http://www.arpalert.org/mysac.html
Source:     	http://www.arpalert.org/src/%{name}-%{version}.tar.gz
Patch0:		mysac-makefile.patch
BuildRequires:  mysql-devel
%if %mdkversion < 200800
BuildRoot:  %{_tmppath}/%{name}-%{version}
%endif

%description
MySAC is a library that provides mechanisms for making asynchronous request to MySQL database.  
It uses uses the official MySQL client library for authentication and network functions. 
Memory allocation must be done in user code, so any memory manager can be used

%package -n     %{libname}
Summary:        Main library for mysac
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
MySAC is a library that provides mechanisms for making asynchronous request to MySQL database.  
It uses uses the official MySQL client library for authentication and network functions. 
Memory allocation must be done in user code, so any memory manager can be used


%package        -n     %{develname}
Summary:        Header files for the dssl library
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Requires:  	mysql-devel

%description    -n %{develname}
MySAC is a library that provides mechanisms for making asynchronous request to MySQL database.
It uses uses the official MySQL client library for authentication and network functions.
Memory allocation must be done in user code, so any memory manager can be used.
These are .h files

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%prep
%setup -q 
%patch0 -p1 -b .makefile
#export LIBS=-lpcap 
#configure2_5x --enable-shared

%build
%make
%{__mkdir_p}  %{buildroot}%{_includedir}
%{__mkdir_p}  %{buildroot}%{_libdir}
%{__install}  -m0755 libmysac.so*  %{buildroot}%{_libdir}
%{__install}  -m0755 libmysac-static.a  %{buildroot}%{_libdir}
%{__install}  -m0755 *.h  %{buildroot}%{_includedir}


%clean
%{__rm} -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libmysac.so.%{major}*


%files  -n %{develname}
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/libmysac.so
%{_libdir}/libmysac-static.a


