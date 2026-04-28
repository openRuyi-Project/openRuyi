# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname libvirt-python
%global pypi_name libvirt_python

Name:           python-libvirt
Version:        12.2.0
Release:        %autorelease
Summary:        Python bindings for libvirt
License:        LGPL-2.1-or-later
URL:            https://libvirt.org
VCS:            git:https://gitlab.com/libvirt/libvirt-python.git
#!RemoteAsset:  sha256:742147988bba7d400f6892beeeb7e0a27758f10ff65421b569b7b4b6a2572e44
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l libvirt libvirtaio libvirt_lxc libvirt_qemu +auto

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(libvirt) >= %{version}
BuildRequires:  pkgconfig(libvirt-lxc) >= %{version}
BuildRequires:  pkgconfig(libvirt-qemu) >= %{version}

Provides:       python3-libvirt = %{version}-%{release}
Provides:       python3-libvirt%{?_isa} = %{version}-%{release}
%python_provide python3-libvirt

%description
The python-libvirt package contains Python bindings that permit applications
written in Python to use the libvirt virtualization API.

%prep -a
# Unset execute bits for example scripts; executable examples can introduce
# spurious automatic interpreter dependencies.
find examples -type f -exec chmod 0644 {} \;

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc AUTHORS ChangeLog README examples/
%license COPYING
%{python3_sitearch}/libvirtmod*.so

%changelog
%autochangelog
