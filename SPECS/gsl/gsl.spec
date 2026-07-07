# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# XXX: This feature should be moved to a more appropriate location.
%bcond llvmir 1

%if %{with llvmir}
  %define __install /var/lib/clang-wrap/install

  %ifarch x86_64
     %global emit_llvmir_flags -march=x86-64-v4
  %elifarch riscv64
     %global emit_llvmir_flags -march=rva23u64
  %else
     %global emit_llvmir_flags 1
  %endif

%global ___build_pre \
        set -x \
        export EMIT_LLVMIR=%{emit_llvmir_flags} \
        export PATH=%{clang_wrap_varlibdir}:$PATH \
        set +x \
        %{?___build_pre}
%global toolchain clang
%endif

Name:           gsl
Version:        2.8
Release:        %autorelease
Summary:        The GNU Scientific Library for numerical analysis
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/gsl/
VCS:            git:https://git.savannah.gnu.org/git/gsl.git
#!RemoteAsset:  sha256:6a99eeed15632c6354895b1dd542ed5a855c0f15d9ad1326c6fe2b2c9e423190
Source0:        https://ftpmirror.gnu.org/gnu/gsl/gsl-%{version}.tar.gz
BuildSystem:    autotools

# https://lists.gnu.org/archive/html/bug-gsl/2026-05/msg00004.html
# Undefined behavior in gsl_pow_int
Patch2000:      2000-Fix-undefined-behavior-in-gsl_pow_int.patch

BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --disable-static
BuildOption(conf):  CFLAGS="%{optflags} -ffp-contract=off"

%if %{with llvmir}
BuildRequires:  clang
BuildRequires:  llvm
BuildRequires:  clang-wrap
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  make

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package        devel
Summary:        Libraries and the header files for GSL development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The gsl-devel package contains the header files necessary for
developing programs using the GSL (GNU Scientific Library).

%conf -p
autoreconf -fiv

%install -a
rm -rf %{buildroot}%{_infodir}/dir

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/gsl-histogram
%{_bindir}/gsl-randist
%{_libdir}/libgsl.so.28*
%{_libdir}/libgslcblas.so.0*
%{_mandir}/man1/gsl-histogram.1*
%{_mandir}/man1/gsl-randist.1*
%if %{with llvmir}
%{clang_wrap_llvmir_bin_dir}/gsl-histogram{,_cmd}
%{clang_wrap_llvmir_bin_dir}/gsl-randist{,_cmd}
%{clang_wrap_llvmir_dir}/libgsl.so.*
%{clang_wrap_llvmir_dir}/libgslcblas.so.*
%endif

%files devel
%{_bindir}/gsl-config
%{_libdir}/libgsl.so
%{_libdir}/libgslcblas.so
%{_libdir}/pkgconfig/gsl.pc
%{_mandir}/man1/gsl-config.1*
%{_mandir}/man3/gsl.3*
%{_infodir}/gsl-ref.info*
%{_datadir}/aclocal/gsl.m4
%{_includedir}/gsl/

%changelog
%autochangelog
