# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname supervisor

Name:           python-%{srcname}
Version:        4.3.0
Release:        %autorelease
Summary:        A system for controlling process state under UNIX
License:        LicenseRef-openRuyi-Supervisor
URL:            http://supervisord.org/
VCS:            git:https://github.com/Supervisor/supervisor.git
#!RemoteAsset:  sha256:4a2bf149adf42997e1bb44b70c43b613275ec9852c3edacca86a9166b27e945e
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# python3-spew is not available in the repository
BuildOption(check):  -e 'supervisor.tests.fixtures.spew'
BuildOption(check):  -e 'supervisor.tests.fixtures.unkillable_spew'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Supervisor is a client/server system that allows its users to monitor and
control a number of processes on UNIX-like operating systems.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSES.txt
%{_bindir}/echo_supervisord_conf
%{_bindir}/pidproxy
%{_bindir}/supervisorctl
%{_bindir}/supervisord

%changelog
%autochangelog
