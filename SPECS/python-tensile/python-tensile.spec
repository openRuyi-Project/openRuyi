# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tensile
%global upstreamname Tensile
%global rocm_version 7.1.1

Name:           python-%{srcname}
Version:        %{rocm_version}
Release:        %autorelease
Summary:        Tool for creating benchmark-driven backend libraries for GEMMs
License:        MIT
URL:            https://github.com/ROCm/Tensile
#!RemoteAsset:  sha256:12e3b538efe2069ecd77dfd0bc9309d6f067eab002f153ddbf8b20896ee46ec3
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{upstreamname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Requires:       cmake-filesystem
Requires:       hipcc
Requires:       rocminfo
Requires:       python3dist(msgpack)
Requires:       python3dist(pyyaml)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%patchlist
0001-fix-python-shebang.patch
0002-fix-tensile-get-path.patch
# TODO: joblib is not enabled on openRuyi
0003-reduce-requirements.patch
0004-ignore-asm-cap-cache.patch
# no bundled clang is used on openRuyi
0005-no-amdclang-when-rocm-llvm-is-unbundled.patch
# /opt is not used on openRuyi packaging
0006-use-system-path-instead-of-default.patch

%description
Tensile is a tool for creating benchmark-driven backend libraries for GEMMs,
GEMM-like problems (such as batched GEMM), and general N-dimensional tensor
contractions on a GPU. The Tensile library is mainly used as backend library to
rocBLAS. Tensile acts as the performance backbone for a wide variety of
'compute' applications running on AMD GPUs.

%prep -a
#Fix a few things:
chmod 755 Tensile/Configs/miopen/convert_cfg.py

%generate_buildrequires
%pyproject_buildrequires

%install -a
# /usr/cmake/* -> /usr/lib/cmake/Tensile
mkdir -p %{buildroot}%{_datadir}/cmake/Tensile
mv %{buildroot}%{_prefix}/cmake/* %{buildroot}%{_datadir}/cmake/Tensile/
rm -rf %{buildroot}%{_prefix}/cmake

# Do not distribute broken bins
rm %{buildroot}%{_bindir}/tensile*

# rm hard links and replace
rm %{buildroot}%{python3_sitelib}/%{upstreamname}/cmake/*.cmake
mv %{buildroot}%{_datadir}/cmake/Tensile/*.cmake %{buildroot}%{python3_sitelib}/%{upstreamname}/cmake/

%pyproject_save_files %{upstreamname}

%check
# 1. tensile requires GPU hardware at runtime
# 2. optional dependencies (joblib) are intentionally excluded

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.md
# Do not distribute tests
%exclude %{python3_sitelib}/%{upstreamname}/Tests
%{_bindir}/Tensile
%{_bindir}/TensileBenchmarkCluster
%{_bindir}/TensileCreateLibrary
%{_bindir}/TensileGetPath
%{_bindir}/TensileRetuneLibrary

%changelog
%autochangelog
