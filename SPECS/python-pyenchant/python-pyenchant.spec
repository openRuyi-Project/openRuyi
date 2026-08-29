# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyenchant

Name:           python-%{srcname}
Version:        3.3.0
Release:        %autorelease
Summary:        Python bindings for Enchant spellchecking library
License:        MIT
URL:            https://github.com/pyenchant/pyenchant
#!RemoteAsset:  sha256:825288246b5debc9436f91967650974ef0d5636458502619e322c476f1283891
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -L enchant
# No module named 'gtk'
BuildOption(check):  -e enchant.checker.GtkSpellCheckerDialog
# No module named 'wx'
BuildOption(check):  -e enchant.checker.wxSpellCheckerDialog

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  enchant

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       enchant

%description
PyEnchant is a spellchecking library for Python, based on the Enchant
library by Dom Lachowicz.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
