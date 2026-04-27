# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname typer

Name:           python-typer
Version:        0.21.1
Release:        %autorelease
Summary:        Typer, build great CLIs. Easy to code. Based on Python type hints
License:        MIT
URL:            https://github.com/fastapi/typer
#!RemoteAsset:  sha256:73495dd08c2d0940d611c5a8c04e91c2a0a98600cbd4ee19192255a233b6dbfd
Source0:        https://files.pythonhosted.org/packages/source/t/typer-slim/typer_slim-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(parso)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pdm-backend)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(rich)
BuildRequires:  python3dist(shellingham)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Typer is a library for building CLI applications that users will
love using and developers will love creating. Based on Python type hints.
It's also a command line tool to run scripts, automatically converting
them to CLI applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/typer

%changelog
%autochangelog
