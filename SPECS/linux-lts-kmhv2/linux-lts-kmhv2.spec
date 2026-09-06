# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Han Gao <gaohan@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Hangfan Li <lihangfan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%ifarch riscv64
%bcond dtbs  1
%else
%bcond dtbs  0
%endif
%bcond rust  1

%global variant_name lts-kmhv2

Name:           linux-lts-kmhv2
Version:        6.18.38
Release:        %autorelease
Summary:        The Linux lts Kernel
License:        GPL-2.0-only
URL:            https://www.kernel.org/
#!RemoteAsset:  sha256:ac26e508abd56e9f8b89872b6e10c49fc823bcc70d8068a5d8504c1a7c4ff045
Source0:        https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz
Source1:        series
Source2:        config.x86_64
Source3:        config.riscv64
Source4:        config.riscv64-rva20

ExclusiveArch:  riscv64

%if "%{?openruyi_riscv_arch}" == "-march=rva20u64"
    %global arch_suffix -rva20
%else
    %global arch_suffix %{nil}
%endif

BuildSystem:    linux
BuildOption(prep):  -n linux-%{version} -p1
BuildOption(conf):  %{_sourcedir}/config.%{_arch}%{arch_suffix}

BuildRequires:  openruyi-linux-build
%linux_package_dependencies

%patchlist
%include %{SOURCE1}

%description
This is the meta package that handles standard %{name} kernel installation.

%linux_package_implementation

%changelog
%autochangelog
