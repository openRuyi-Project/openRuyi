# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cffsubr

Name:           python-%{srcname}
Version:        0.4.0
Release:        %autorelease
Summary:        Standalone CFF subroutinizer based on AFDKO tx
License:        Apache-2.0
URL:            https://github.com/adobe-type-tools/cffsubr
VCS:            git:https://github.com/adobe-type-tools/cffsubr
#!RemoteAsset:  sha256:2c321b6807bd95856d921ed9dce8506495cf49fc7a89a63cb942e8bece13addd
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:0ed13668906e86dbc0dcddf30fdee68c10203dea4e83852b4edb810821bee3c4
Source1:        https://www.antlr.org/download/antlr4-cpp-runtime-4.13.2-source.zip
BuildSystem:    pyproject

# Use offline ANTLR archive and fix old CMake policy settings in bundled AFDKO.
Patch0:         0001-afdko-use-antlr4-archive-from-env.patch
# Avoid pip downloading python-cmake/python-ninja from setup_requires.
Patch1:         0002-afdko-drop-python-cmake-ninja-setup-requires.patch

BuildOption(install):  -l %{srcname} +auto
# cffsubr custom backend injects python3dist(cmake/ninja); we keep system
# cmake/ninja in BuildRequires and disable dynamic pyproject BR generation.
BuildOption(generate_buildrequires):  -N

BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  ninja
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(scikit-build)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-git-ls-files)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
BuildRequires:  utf8cpp

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
cffsubr is a standalone CFF subroutinizer based on the AFDKO tx tool.

%build -p
export ANTLR4_ZIP_REPOSITORY=%{SOURCE1}
export FORCE_SYSTEM_LIBXML2=1

%files -f %{pyproject_files}
%doc README.md
%license LICENSE NOTICE
%{_bindir}/cffsubr

%changelog
%autochangelog
