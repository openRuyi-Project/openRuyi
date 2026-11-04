# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tmt

Name:           python-%{srcname}
Version:        1.80.0
Release:        %autorelease
Summary:        Test Management Tool
License:        MIT
URL:            https://github.com/teemtee/tmt
#!RemoteAsset:  sha256:92decab8ae98c740b37b04cce13234dd4938b0692ee492ff6c22bf7137b96f59
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
BuildRequires:  git-core
BuildRequires:  rsync

Requires:       git-core
Requires:       libvirt-daemon-driver-qemu
Requires:       mock
Requires:       openssh-clients
Requires:       podman
Requires:       python3dist(ansible-core)
Requires:       python3dist(libvirt-python)
Requires:       python3dist(testcloud) >= 0.12
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

%install -a
# Build the man page from the upstream overview without Sphinx directives.
{ cat docs/header.txt; tail -n +8 docs/overview.rst; } |
    sed '/versionadded::/d' > tmt-man.rst
install -d %{buildroot}%{_mandir}/man1
rst2man tmt-man.rst %{buildroot}%{_mandir}/man1/tmt.1
install -Dpm0644 completions/bash/tmt %{buildroot}%{_datadir}/bash-completion/completions/tmt

%check -a
# Exercise CLI initialization and discovery with the upstream mini example.
# The pytest harness imports pytest-container even for these offline cases.
export PYTHONPATH=%{buildroot}%{python3_sitelib}
check_dir=$(mktemp -d)
mkdir "$check_dir/metadata"
%{buildroot}%{_bindir}/tmt init "$check_dir/metadata"
test -s "$check_dir/metadata/.fmf/version"
%{buildroot}%{_bindir}/tmt --root "$PWD/examples/mini" run --id "$check_dir/run" discover > tmt-check.log 2>&1
cat tmt-check.log
grep -F '1 test selected' tmt-check.log

%files -f %{pyproject_files}
%doc examples README.rst
%{_bindir}/tmt
%{_datadir}/bash-completion/completions/tmt
%{_mandir}/man1/tmt.1*

%changelog
%autochangelog
