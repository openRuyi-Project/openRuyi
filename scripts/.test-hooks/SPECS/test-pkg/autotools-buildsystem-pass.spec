Name: test-autotools-bs
Version: 1.0
Release: 1
Summary: test
BuildSystem: autotools

%prep
autoreconf -fiv

%build
%configure
%make_build

%files
%{_libdir}/libtest.so
