Name: test-autotools-no-autoreconf
Version: 1.0
Release: 1
Summary: test

%build
%configure
%make_build

%files
%{_libdir}/libtest.so
