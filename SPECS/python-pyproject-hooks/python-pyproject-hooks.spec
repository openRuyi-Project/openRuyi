# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyproject_hooks

Name:           python-pyproject-hooks
Version:        1.2.0
Release:        %autorelease
Summary:        Low-level library for calling pyproject.toml backends
License:        MIT
URL:            https://github.com/pypa/pyproject-hooks
#!RemoteAsset:  sha256:1e859bd5c40fae9448642dd871adf459e5e2084186e8d2c2a79a824c970da1f8
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-pyproject-hooks = %{version}-%{release}
%python_provide python3-pyproject-hooks

%description
pyproject-hooks is a low-level library for calling build backends
in pyproject.toml-based projects.  It provides basic functionality to
write tooling that generates distribution files from Python projects.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
