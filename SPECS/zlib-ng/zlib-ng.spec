# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond zlib_compat 1
%bcond systemtap 0

Name:           zlib-ng
Version:        2.2.5
Release:        %autorelease
Summary:        Zlib replacement with SIMD optimizations
License:        Zlib
URL:            https://github.com/zlib-ng/zlib-ng
#!RemoteAsset
Source:         https://github.com/zlib-ng/zlib-ng/archive/refs/tags/%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf): -DINSTALL_LIB_DIR=%{_libdir}
BuildOption(conf): -DWITH_RVV:BOOL=ON
BuildOption(conf): -DWITH_GTEST:BOOL=OFF
BuildOption(conf): -DWITH_NEW_STRATEGIES:BOOL=OFF
BuildOption(conf): -DWITH_ARMV6:BOOL=OFF
%if %{with zlib_compat}
BuildOption(conf): -DZLIB_COMPAT:BOOL=ON
%else
BuildOption(conf): -DZLIB_COMPAT:BOOL=OFF
%endif

BuildRequires:  cmake gcc gcc-c++
%if %{with systemtap}
BuildRequires:  systemtap-sdt-devel
%endif

%description
zlib-ng is a zlib replacement with support for CPU intrinsics.
%if %{with zlib_compat}
This package provides a drop-in zlib-compatible library.
%endif

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
%if %{with zlib_compat}
Conflicts:      zlib-devel
Provides:       zlib-devel = %{version}
%endif

%description    devel
The %{name}-devel package contains header files and development libraries for zlib-ng.


%install -a
%if %{with zlib_compat}
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
mkdir -p %{buildroot}%{_libdir}/zlib-ng-compat
(cat > %{buildroot}%{_sysconfdir}/ld.so.conf.d/zlib-ng-compat-%{_arch}.conf) <<-EOF
	%{_libdir}/zlib-ng-compat
	EOF
cd %{buildroot}%{_libdir}/
	mv libz.so.* zlib-ng-compat/
	ln -sf zlib-ng-compat/libz.so.1 libz.so
%endif

%files
%license LICENSE.md
%doc README.md
%if %{with zlib_compat}
%config %{_sysconfdir}/ld.so.conf.d/zlib-ng-compat-%{_arch}.conf
%{_libdir}/libz.so*
%{_libdir}/zlib-ng-compat/libz.so*
%else
%{_libdir}/libz-ng.so.2*
%endif

%files devel
%if %{with zlib_compat}
%{_includedir}/zconf.h
%{_includedir}/zlib.h
%{_includedir}/zlib_name_mangling.h
%{_libdir}/libz.so
%{_libdir}/pkgconfig/zlib.pc
%{_libdir}/cmake/ZLIB/
%else
%{_includedir}/zconf-ng.h
%{_includedir}/zlib-ng.h
%{_includedir}/zlib_name_mangling-ng.h
%{_libdir}/libz-ng.so
%{_libdir}/pkgconfig/zlib-ng.pc
%{_libdir}/cmake/zlib-ng/
%endif

%changelog
%{?autochangelog}
