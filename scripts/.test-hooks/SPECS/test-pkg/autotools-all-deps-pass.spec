Name: test-autotools-ok
Version: 1.0
Release: 1
Summary: test
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%prep
autoreconf -fiv

%build
%configure
%make_build

%files
%{_libdir}/libtest.so
