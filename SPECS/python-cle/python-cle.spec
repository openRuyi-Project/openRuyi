# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cle
%global commit c349c5353c70d1e1d3ec538fcb60d45801cc939d

Name:           python-%{srcname}
Version:        9.2.193
Release:        %autorelease
Summary:        CLE Loads Everything
License:        BSD-2-Clause
URL:            https://github.com/angr/cle
#!RemoteAsset:  sha256:5551287b59c4b30e25e872b8280932e7702077aab8016232bb0405c5cf73f0c3
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
# test data all depend on this binaries repository.
# the commit version is 9.2.193, which matches the CLE version.
#!RemoteAsset:  sha256:47e612ac93f3cab7f0f803dd393ca4ff79ec7f332ad59a0883c4c9e22b1cba56
Source1:        https://github.com/angr/binaries/archive/%{commit}/binaries-%{commit}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# https://github.com/angr/cle/pull/637
Patch0:         0001-riscv64-init-support.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(archinfo)
BuildRequires:  python3dist(arpy)
BuildRequires:  python3dist(pefile)
BuildRequires:  python3dist(pyelftools)
BuildRequires:  python3dist(pyvex) == 9.2.193
BuildRequires:  python3dist(sortedcontainers)
BuildRequires:  python3dist(minidump)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
CLE loads binaries and their associated libraries, resolves
imports and provides an abstraction of process memory the
same way as if it was loader by the OS's loader.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
cd %{_builddir}/%{name}-%{version}
tar -xf %{SOURCE1}
chmod -R 755 binaries-%{commit}
mv binaries-%{commit} ../binaries

# pyxdia is not important for our Linux
# and it is depend on blink which is just
# a repo writen by author
# (It doesn't support riscv)
# https://github.com/mborgerson/xdia/tree/main/pyxdia
# https://github.com/mborgerson/blink/
# we ignore it by removing the dependency and patching the code(Not used much)
sed -i '/pyxdia/d' pyproject.toml
sed -i 's/^import pyxdia/# import pyxdia/' cle/backends/pe/pe.py
sed -i 's/pdb = pyxdia.PDB(pdb_path)/raise NameError/' cle/backends/pe/pe.py
# minidump is used for windows's dump files
# https://github.com/skelsec/minidump
sed -i '/minidump/d' pyproject.toml
sed -i 's/arpy==1.1.1/arpy>=1.1.1/' pyproject.toml

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%{?autochangelog}
