Summary:	Template engine library
Name:		ctpl
Version:	0.3.3
Release:	1
License:	GPL v3
Group:		Libraries
Source0:	http://download.tuxfamily.org/ctpl/releases/%{name}-%{version}.tar.gz
# Source0-md5:	3380e06d94d921fb50b0e40ddb351daa
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package devel
Summary:	Header files for CTPL library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for CTPL library.

%package apidocs
Summary:	CTPL API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
CTPL API documentation.

%prep
%setup -q

# don't fail on AM warnings
%{__sed} -i 's/-Werror//' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/ctpl
%attr(755,root,root) %ghost %{_libdir}/libctpl.so.2
%attr(755,root,root) %{_libdir}/libctpl.so.*.*.*
%{_mandir}/man1/ctpl.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libctpl.so
%{_includedir}/ctpl
%{_pkgconfigdir}/ctpl.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/ctpl

