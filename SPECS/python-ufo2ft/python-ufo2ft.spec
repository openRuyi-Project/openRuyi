# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ufo2ft

Name:           python-%{srcname}
Version:        3.7.0
Release:        %autorelease
Summary:        Bridge between UFOs and FontTools
License:        MIT
URL:            https://github.com/googlefonts/ufo2ft
VCS:            git:https://github.com/googlefonts/ufo2ft
#!RemoteAsset:  sha256:e467db380d42774d4a6016a13879987d76f921c5d62cc3cc78960da019f1e80e
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l ufo2ft +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(booleanoperations) >= 0.9
BuildRequires:  python3dist(cffsubr) >= 0.3
BuildRequires:  python3dist(fontmath) >= 0.9.4
BuildRequires:  python3dist(fonttools) >= 4.61.1
BuildRequires:  python3dist(fonttools[ufo]) >= 4.61.1
BuildRequires:  python3dist(ufolib2) >= 0.18.1
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%pyproject_extras_subpkg -n python-%{srcname} cffsubr compreffor pathops

%description
ufo2ft is a bridge between UFOs and FontTools.

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
