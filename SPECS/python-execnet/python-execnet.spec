# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname execnet

%bcond doc 0

Name:           python-%{srcname}
Version:        2.1.2
Release:        %autorelease
Summary:        Distributed Python deployment and communication
License:        MIT AND GPL-2.0-or-later
URL:            http://codespeak.net/execnet
#!RemoteAsset:  sha256:63d83bfdd9a23e35b9c6a3261412324f964c2ec8dcd8d3c6916ee9373e0befcd
Source0:        https://files.pythonhosted.org/packages/source/e/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# We don't have python-servicemanager yet
BuildOption(check):  -e execnet.script.quitserver
BuildOption(check):  -e execnet.script.shell
BuildOption(check):  -e execnet.script.socketserverservice

BuildRequires:  pyproject-rpm-macros
BuildRequires:  procps-ng
BuildRequires:  pkgconfig(python3)
%if %{with doc}
BuildRequires:  make
BuildRequires:  sphinx-build
%endif
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
execnet provides a share-nothing model with channel-send/receive
communication for distributing execution across many Python
interpreters across version, platform and network barriers. It has a
minimal and fast API targetting the following uses:

 * distribute tasks to (many) local or remote CPUs
 * write and deploy hybrid multi-process applications
 * write scripts to administer multiple environments

%prep -a
# remove shebangs and fix permissions
find . -type f -a \( -name '*.py' -o -name 'py.*' \) \
   -exec sed -i '1{/^#!/d}' {} \; \
   -exec chmod u=rw,go=r {} \;

%generate_buildrequires
%pyproject_buildrequires

%build -p
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%build -a
%if %{with doc}
make -C doc html PYTHONPATH=$(pwd)/src
# remove hidden file
rm doc/_build/html/.buildinfo
%endif

%install -p
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%check -a
%pytest -k "not gevent and not eventlet and not test_dont_write_bytecode" testing

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
