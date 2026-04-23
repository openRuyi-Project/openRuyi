# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname blivet

Name:           python-blivet
Version:        3.13.1
Release:        %autorelease
Summary:        Blivet is a python module for system storage configuration.
License:        LGPL-2.1-or-later
URL:            https://github.com/storaged-project/blivet
#!RemoteAsset:  sha256:68d981b900f92637c636dfd3d7b93c698b3b1a2112649a95b43bac385f61bf1c
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  gettext
BuildRequires:  pkgconfig(python3)

Requires:       parted
Requires:       python3-blockdev
Requires:       python3-bytesize
Requires:       python3dist(dasbus)
Requires:       python3-libmount
Requires:       python3dist(pygobject)
Requires:       python3dist(pyparted)
Requires:       python3dist(pyudev)
Requires:       python3dist(selinux)
Requires:       util-linux
Requires:       lsof
Requires:       systemd-udev

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The python-blivet package is a python module for examining and modifying
storage configuration.

%generate_buildrequires
%pyproject_buildrequires

# No configure
%conf

%install -a
# TODO: Avoid illegal package names
rm -rf %{buildroot}%{_datadir}/locale/*@*
%find_lang %{srcname} --generate-subpackages

# TODO: check needs ton of other dependencies - 251
%check

%files -f %{srcname}.lang
%doc README.md ChangeLog examples
%license COPYING
%{python3_sitelib}/*
%{_sysconfdir}/dbus-1/system.d/*
%{_datadir}/dbus-1/system-services/*
%{_libexecdir}/*
%{_unitdir}/*

%changelog
%autochangelog
