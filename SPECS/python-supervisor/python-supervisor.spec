# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname supervisor
%global pkgname supervisor

Name:           python-%{srcname}
Version:        4.2.5
Release:        %autorelease
Summary:        A system for controlling process state under UNIX
License:        BSD-derived
URL:            http://supervisord.org/
#!RemoteAsset:  sha256:34761bae1a23c58192281a5115fb07fbf22c9b0133c08166beffc70fed3ebc12
Source0:        https://files.pythonhosted.org/packages/source/s/supervisor/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install):  -l %{pkgname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Supervisor is a client/server system that allows its users to monitor and
control a number of processes on UNIX-like operating systems.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{pkgname}-%{version}

rm -rf supervisor/tests

%files -f %{pyproject_files}
%{_bindir}/supervisord
%{_bindir}/supervisorctl
%{_bindir}/echo_supervisord_conf
%{_bindir}/pidproxy
%license LICENSES.txt COPYRIGHT.txt

%changelog
%autochangelog
