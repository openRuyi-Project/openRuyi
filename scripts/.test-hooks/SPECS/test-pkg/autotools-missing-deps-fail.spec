Name: test-autotools-missing-deps
Version: 1.0
Release: 1
Summary: test

%prep
autoreconf -fiv

%build
%configure
%make_build

%files
%{_libdir}/libtest.so
