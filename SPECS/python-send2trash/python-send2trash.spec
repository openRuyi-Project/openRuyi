# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname send2trash
%global pypi_name send2trash

Name:           python-%{srcname}
Version:        2.1.0
Release:        %autorelease
Summary:        Send files to the trash natively
License:        BSD-3-Clause
URL:            https://github.com/arsenetar/send2trash
#!RemoteAsset:  sha256:1c72b39f09457db3c05ce1d19158c2cbef4c32b8bedd02c155e49282b7ea7459
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l send2trash
# https://github.com/arsenetar/send2trash/issues/110
BuildOption(check):  -e 'send2trash.mac'
BuildOption(check):  -e 'send2trash.mac.legacy'
BuildOption(check):  -e 'send2trash.mac.modern'
BuildOption(check):  -e 'send2trash.win'
BuildOption(check):  -e 'send2trash.win.IFileOperationProgressSink'
BuildOption(check):  -e 'send2trash.win.legacy'
BuildOption(check):  -e 'send2trash.win.modern'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Send2Trash sends files and directories to the platform trash directory.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/send2trash

%changelog
%autochangelog
