# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pytest_freezer

Name:           python-pytest-freezer
Version:        0.4.9
Release:        %autorelease
License:        MIT
URL:            https://github.com/pytest-dev/pytest-freezer/
Summary:        Pytest plugin providing a fixture interface for spulec/freezegun
Provides:       python3-pytest-freezer
%python_provide python3-pytest-freezer
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildSystem:    pyproject
BuildOption(install): -l %{srcname} +auto
%description
Pytest plugin providing a fixture interface for
@url{https://github.com/spulec/freezegun, freezegun}.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%autochangelog
