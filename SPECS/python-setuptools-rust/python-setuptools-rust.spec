# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname setuptools_rust

Name:           python-setuptools-rust
Version:        1.11.1
Release:        %autorelease
Summary:        Setuptools Rust extension plugin
License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(semantic-version)

Provides:       python3-setuptools-rust
%python_provide python3-setuptools-rust

%description
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
