# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname xgrammar

Name:           python-%{srcname}
Version:        0.1.33
Release:        %autorelease
Summary:        Fast, Flexible and Portable Structured Generation
License:        Apache-2.0
URL:            https://github.com/mlc-ai/xgrammar
#!RemoteAsset:  sha256:8dbe5fc3d76651ab1fac7a68fc2a118b885fa0ec7189927fb6e0dce0081aea99
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L
# No module named 'triton'
BuildOption(check):  -e xgrammar.kernels.apply_token_bitmask_inplace_triton
BuildOption(check):  -e xgrammar.kernels.apply_token_bitmask_inplace_cuda
# No module named 'mlx'
BuildOption(check):  -e xgrammar.kernels.apply_token_bitmask_mlx
BuildOption(check):  -e xgrammar.contrib.mlxlm

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  cmake
BuildRequires:  ninja

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Efficient, Flexible and Portable Structured Generation.

%prep -a
sed -i 's/nanobind==2\.5\.0/nanobind>=2.5.0/g' pyproject.toml
sed -i 's/-Werror//g' CMakeLists.txt
# Exclude x86-only Triton dependency for RISC-V compatibility.
sed -i '/triton/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
