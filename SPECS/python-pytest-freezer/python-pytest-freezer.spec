# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest_freezer

Name:           python-pytest-freezer
Version:        0.4.9
Release:        %autorelease
Summary:        Pytest plugin providing a fixture interface for spulec/freezegun
License:        MIT
URL:            https://github.com/pytest-dev/pytest-freezer/
#!RemoteAsset:  sha256:21bf16bc9cc46bf98f94382c4b5c3c389be7056ff0be33029111ae11b3f1c82a
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-pytest-freezer = %{version}-%{release}
%python_provide python3-pytest-freezer

%description
Pytest plugin providing a fixture interface for
https://github.com/spulec/freezegun.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
