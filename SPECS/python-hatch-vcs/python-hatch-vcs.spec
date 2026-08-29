# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hatch_vcs

Name:           python-hatch-vcs
Version:        0.5.0
Release:        %autorelease
Summary:        Hatch plugin for versioning with your preferred VCS
License:        MIT
URL:            https://github.com/ofek/hatch-vcs
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset:  sha256:0395fa126940340215090c344a2bf4e2a77bcbe7daab16f41b37b98c95809ff9
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l hatch_vcs

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pluggy)
BuildRequires:  python3dist(setuptools-scm)

Provides:       python3-hatch-vcs = %{version}-%{release}
%python_provide python3-hatch-vcs

%description
This provides a plugin for Hatch that uses your preferred version control
system (like Git) to determine project versions.

%files -f %{pyproject_files}
%doc README.md HISTORY.md

%changelog
%autochangelog
