# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyxdg

Name:           %{srcname}
Version:        0.28
Release:        %autorelease
Summary:        Python library to access freedesktop.org standards
License:        LGPL-2.0-only
URL:            https://freedesktop.org/wiki/Software/pyxdg/
VCS:            git:https://gitlab.freedesktop.org/xdg/pyxdg
# Upstream did not include the test/examples directory in the source tarball
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# https://gitlab.freedesktop.org/xdg/pyxdg/-/commit/9291d419017263c922869d79ac1fe8d423e5f929
Patch0:         0001-menu-handle-python-3.14-ast.Str-changes.patch

BuildOption(install): -l xdg

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
PyXDG is a python library to access freedesktop.org standards.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%license COPYING
%doc AUTHORS ChangeLog README TODO

%changelog
%autochangelog
