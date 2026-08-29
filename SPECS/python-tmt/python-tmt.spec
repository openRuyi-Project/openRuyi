# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tmt

Name:           python-%{srcname}
Version:        1.72.0
Release:        %autorelease
Summary:        Test Management Tool
License:        MIT
URL:            https://github.com/teemtee/tmt
#!RemoteAsset:  sha256:df9b33cc10aae202b679b44933661dd34447ba248df8f02b5b6579334134958a
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(fmf)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pint)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(ruamel-yaml)
BuildRequires:  python3dist(ruamel-yaml-clib)
BuildRequires:  python3dist(urllib3)

Requires:       git-core
Requires:       libvirt-daemon-driver-qemu
Requires:       mock
Requires:       openssh-clients
Requires:       podman
Requires:       python3dist(ansible-core)
Requires:       python3dist(libvirt-python)
Requires:       python3dist(testcloud)
Requires:       qemu
Requires:       rsync
Requires:       sshpass

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The tmt Python module and command line tool implement the test metadata
specification and provide test execution across multiple environments.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc examples
%doc README.rst
%license LICENSE
%{_bindir}/tmt

%changelog
%autochangelog
