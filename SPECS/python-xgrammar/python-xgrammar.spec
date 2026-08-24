# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname xgrammar

Name:           python-%{srcname}
Version:        0.2.1
Release:        %autorelease
Summary:        Fast, Flexible and Portable Structured Generation
License:        Apache-2.0
URL:            https://github.com/mlc-ai/xgrammar
#!RemoteAsset:  sha256:4c48c251b75d211e9ffa7f4f4ac8b5b0164f89fd5f0d1883ad7ff4554922030d
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}
# No module named 'triton'
BuildOption(check):  -e xgrammar.kernels.apply_token_bitmask_inplace_triton
BuildOption(check):  -e xgrammar.kernels.apply_token_bitmask_inplace_cuda
# No module named 'mlx'
BuildOption(check):  -e xgrammar.kernels.apply_token_bitmask_mlx
BuildOption(check):  -e xgrammar.contrib.mlxlm
# Native shared library
BuildOption(check):  -e xgrammar.libxgrammar_bindings

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
sed -i 's/-Werror//g' CMakeLists.txt

%generate_buildrequires
%pyproject_buildrequires

%install -a
# tvm_ffi uses wheel RECORD metadata to locate the native binding library.
echo '%{srcname}/libxgrammar_bindings.so,,' > \
    %{buildroot}%{python3_sitearch}/%{srcname}-%{version}.dist-info/RECORD

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{python3_sitearch}/%{srcname}-%{version}.dist-info/RECORD

%changelog
%autochangelog
