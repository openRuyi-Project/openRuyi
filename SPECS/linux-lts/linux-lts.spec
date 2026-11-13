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

%global variant_name lts

# Managed under kernel-team-tools
%global patchset_release 4
%global config_version 0

Name:           linux-lts
Version:        6.18.63
Release:        %{patchset_release}.%{config_version}_%autorelease
Summary:        The Linux lts Kernel
License:        GPL-2.0-only
URL:            https://www.kernel.org/
#!RemoteAsset:  sha256:81764a545072d160748beff4d9de2e7d95aa9f16e8261110288f067a2cc61d71
Source0:        https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz
#!RemoteAsset:  sha256:c55b6cd0492638c573c0a4c189f1924322169ebd24e005131cb6c88fcb30996d
Source1:        https://github.com/openRuyi-Project/kernel-team-tools/releases/download/v%{version}-%{patchset_release}.%{config_version}/%{name}-v%{version}-%{patchset_release}.tar.gz
%if "%{?openruyi_riscv_arch}" == "-march=rva20u64"
    %global arch_suffix -rva20
%else
    %global arch_suffix %{nil}
%endif
BuildSystem:    linux

# Extracted within %%prep
BuildOption(conf):  %{_sourcedir}/defconfig

BuildRequires:  openruyi-linux-build
%linux_package_dependencies

%description
This is the meta package that handles standard %{name} kernel installation.

%linux_package_implementation

%prep
%setup -n linux-%{version}
patchset_dir=.openruyi-patchset
mkdir "${patchset_dir}"
tar -xf "%{SOURCE1}" -C "${patchset_dir}"
while IFS= read -r patch_name; do
    echo "Applying patch: ${patch_name}"
    patch -p1 < "${patchset_dir}/${patch_name}" || exit 1
done < "${patchset_dir}/series"

%if "%{?openruyi_riscv_arch}" == "-march=rva20u64"
    %define arch_suffix -rva20
%else
    %define arch_suffix -generic
%endif
cp -v "${patchset_dir}/config.%{_arch}%{arch_suffix}" %{_sourcedir}/defconfig

%changelog
%autochangelog
