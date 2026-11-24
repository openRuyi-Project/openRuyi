# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname mindact
%global commit 5e6483c1a052b4c7c3b45d324c8f23646fb9e274

Name:           python-mindact
Version:        0.1.0
Release:        %autorelease
Summary:        Toolkit for embodied policy training and evaluation
License:        Apache-2.0
URL:            https://github.com/candle-org/MindAct
#!RemoteAsset:  sha256:13c3e109fdee6358a458edfeb828f8bb9c7fd8d7c1b22e0084c1ab7e53e6f181
Source0:        https://github.com/candle-org/MindAct/archive/%{commit}/mindact-%{commit}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Allow the NumPy version shipped with the system Python.
Patch2000:      2000-allow-numpy-2.4.patch

BuildOption(prep):  -n MindAct-%{commit}
BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(numpy) >= 2
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml) >= 6
BuildRequires:  python3dist(setuptools) >= 77

%description
MindAct provides config validation, provenance tracking, evaluation records,
and adapters for embodied AI policies.

%check
%pytest -q

%files -f %{pyproject_files}
%{_bindir}/mindact
%doc README.md

%changelog
%autochangelog
