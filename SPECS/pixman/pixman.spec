# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: YunQiang <yunqiang@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond llvmir 1
%if %{with llvmir}
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

Name:           pixman
Version:        0.46.4
Release:        %autorelease
Summary:        Pixel manipulation library
License:        MIT
URL:            https://gitlab.freedesktop.org/pixman/pixman
#!RemoteAsset:  sha256:d09c44ebc3bd5bee7021c79f922fe8fb2fb57f7320f55e97ff9914d2346a591c
Source:         https://www.cairographics.org/releases/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  --auto-features=auto

%if %{with llvmir}
BuildRequires:  clang
BuildRequires:  llvm
BuildRequires:  clang-wrap
%endif
BuildRequires:  meson

%description
Pixman is a pixel manipulation library for X and cairo. This package contains
the runtime shared library.

%package        devel
Summary:        Development files for the Pixel Manipulation library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config file, and other development
files for the pixman library.

%check
# Disable check because some unit tests demand too much compute power

%if %{with llvmir}
%install -a
%{_libdir}/clang-wrap/bin/meson-install %{_vpath_builddir}/meson-info/intro-installed.json %{buildroot}
%endif

%files
%license COPYING
%{_libdir}/libpixman-1.so.*
%if %{with llvmir}
%{clang_wrap_llvmir_dir}/libpixman-1.so.*
%endif

%files devel
%{_includedir}/pixman-1
%{_libdir}/libpixman-1.so
%{_libdir}/pkgconfig/pixman-1.pc

%changelog
%autochangelog
