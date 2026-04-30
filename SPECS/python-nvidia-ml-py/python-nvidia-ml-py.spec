# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname nvidia-ml-py
%global pypi_name nvidia_ml_py

Name:           python-%{srcname}
Version:        13.595.45
Release:        %autorelease
Summary:        Python bindings for the NVIDIA Management Library
License:        BSD-3-Clause
URL:            https://forums.developer.nvidia.com
#!RemoteAsset:  sha256:c9f34897fe0441ff35bc8f35baf80f830a20b0f4e6ce71e0a325bc0e66acf079
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# modname
BuildOption(install):  -l pynvml -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
nvidia-ml-py provides Python bindings for the NVIDIA Management Library.

%prep -a
cat > pyproject.toml <<'EOF'
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
EOF

%generate_buildrequires
%pyproject_buildrequires

%install -a
rm -f %{buildroot}%{python3_sitelib}/example.py
rm -f %{buildroot}%{python3_sitelib}/__pycache__/example.*.pyc

%files -f %{pyproject_files}
%license README.txt

%changelog
%autochangelog
