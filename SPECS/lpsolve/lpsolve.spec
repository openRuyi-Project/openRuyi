# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lpsolve
Version:        5.5.2.14
Release:        %autorelease
Summary:        Linear and mixed integer programming solver
License:        LGPL-2.1-only
URL:            https://github.com/lp-solve/lp_solve
#!RemoteAsset:  sha256:a4bbdc881128bdbe920a38e134c9add5db47f9aa814a0a018ba940b0f3c278c3
Source0:        %{url}/releases/download/%{version}/lp_solve_%{version}_source.tar.gz
# Link lp_MDO.c to system COLAMD and set the shared library's ABI SONAME.
Patch2000:      2000-use-system-colamd-in-posix-build.patch

BuildRequires:  pkgconfig(COLAMD)

%description
lp_solve optimizes linear objectives subject to linear constraints and
supports both continuous and integer variables.

%package        devel
Summary:        C interface for lp_solve
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and the linker file for applications embedding the lp_solve
optimizer.

%prep
%autosetup -p1 -n lp_solve

# Upstream uses lpsolve55/ccc, with no configure script, Makefile or install target.
%build
export CC=%{__cc} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"
export COLAMD_CFLAGS="$(pkg-config --cflags COLAMD)"
export COLAMD_LIBS="$(pkg-config --libs COLAMD)"
(cd lpsolve55 && sh ccc)
libdir="$PWD/lpsolve55/bin/ux%{__isa_bits}"
ln -s liblpsolve55.so "$libdir/liblpsolve55.so.5.5"
%{__cc} %{build_cflags} -I. -Ishared -DPARSER_LP lp_solve/lp_solve.c \
    %{build_ldflags} -L"$libdir" -llpsolve55 -lm -ldl -o lp_solve_cli

%install
install -Dpm 0755 lp_solve_cli %{buildroot}%{_bindir}/lp_solve
install -Dpm 0755 lpsolve55/bin/ux%{__isa_bits}/liblpsolve55.so \
    %{buildroot}%{_libdir}/liblpsolve55.so.%{version}
ln -s liblpsolve55.so.%{version} %{buildroot}%{_libdir}/liblpsolve55.so.5.5
ln -s liblpsolve55.so.5.5 %{buildroot}%{_libdir}/liblpsolve55.so
install -d %{buildroot}%{_includedir}/lpsolve
install -pm 0644 declare.h fortify.h lp_fortify.h lp_Hash.h lp_lib.h \
    lp_matrix.h lp_mipbb.h lp_SOS.h lp_types.h lp_utils.h %{buildroot}%{_includedir}/lpsolve/

%files
%doc README.txt
%license LICENSE
%{_bindir}/lp_solve
%{_libdir}/liblpsolve55.so.*

%files devel
%{_includedir}/lpsolve/
%{_libdir}/liblpsolve55.so

%changelog
%autochangelog
