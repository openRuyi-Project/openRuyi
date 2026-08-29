# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname progressbar2

Name:           python-%{srcname}
Version:        4.5.0
Release:        %autorelease
Summary:        Library to provide visual progress to long running operations
License:        BSD-3-Clause
URL:            https://github.com/WoLpH/python-progressbar
#!RemoteAsset:  sha256:6662cb624886ed31eb94daf61e27583b5144ebc7383a17bae076f8f4f59088fb
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l progressbar
BuildOption(check):  -e progressbar.terminal.os_specific.windows

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(freezegun)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A text progress bar is typically used to display the progress of a long running
operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of the line
is given by a number of widgets.

The progressbar module is very easy to use, yet very powerful. It will also
automatically enable features like auto-resizing when the system supports it.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_bindir}/progressbar

%changelog
%autochangelog
