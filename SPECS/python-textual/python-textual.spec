# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname textual

Name:           python-%{srcname}
Version:        8.2.6
Release:        %autorelease
Summary:        Modern Text User Interface framework
License:        MIT
URL:            https://github.com/Textualize/textual
#!RemoteAsset:  sha256:cef3714498a120a99278b98d4c165c278844e73db50f1db039aaabd89f2d1b63
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# missing python3dist(markdown-it-py[linkify])
Patch2000:      2000-remove-linkify-extra.patch

BuildOption(install):  -l textual
# Windows-specific drivers, not available on Linux
BuildOption(check):  -e 'textual.drivers.win32'
BuildOption(check):  -e 'textual.drivers.windows_driver'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(mdit-py-plugins)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(platformdirs)
BuildRequires:  python3dist(poetry-core)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(rich)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Textual is a Text User Interface (TUI) framework for Python.
It allows developers to build interactive terminal applications.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
