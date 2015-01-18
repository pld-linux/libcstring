Summary:	Library to support cross-platform C string functions
Summary(pl.UTF-8):	Biblioteka do obsługi wieloplatformowych funkcji na łańcuchach C
Name:		libcstring
Version:	20150101
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libcstring/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	79652b81cd3b97a1b4f31442a224b78d
URL:		https://github.com/libyal/libcstring/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcstring is a library for cross-platform C string functions.

%description -l pl.UTF-8
libcstring to wieloplatformowa biblioteka funkcji obsługujących
łańcuchy C.

%package devel
Summary:	Header files for libcstring library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcstring
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcstring library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcstring.

%package static
Summary:	Static libcstring library
Summary(pl.UTF-8):	Statyczna biblioteka libcstring
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcstring library.

%description static -l pl.UTF-8
Statyczna biblioteka libcstring.

%prep
%setup -q

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcstring.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcstring.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcstring.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcstring.so
%{_includedir}/libcstring
%{_includedir}/libcstring.h
%{_pkgconfigdir}/libcstring.pc
%{_mandir}/man3/libcstring.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcstring.a
