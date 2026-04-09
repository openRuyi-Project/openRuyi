# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global xyz_version 3.17.4
%global xy_version %(sed 's/\\(.*\\)\\..*/\\1/'<<<%{xyz_version})

Name:           fuse3
Version:        %{xyz_version}
Release:        %autorelease
Summary:        File System in Userspace (FUSE) v3 utilities
License:        GPL-1.0-or-later
URL:            http://fuse.sf.net
VCS:            git:https://github.com/libfuse/libfuse
#!RemoteAsset
Source0:        https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.gz.sig
# Our little stupid config file
Source2:        fuse.conf
BuildSystem:    meson

BuildOption(conf):  -D udevrulesdir=%{_udevrulesdir}
BuildOption(conf):  -D useroot=false

BuildRequires:  libselinux-devel
BuildRequires:  ninja
BuildRequires:  meson

Provides:       %{name}-libs = %{version}-%{release}

Requires:       fuse-common

%description
With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains the FUSE v3 userspace tools to
mount a FUSE filesystem.

%package        devel
Summary:        File System in Userspace (FUSE) v3 devel files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
License:        LGPL-2.1-or-later

%description    devel
With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains development files (headers,
pgk-config) to develop FUSE v3 based applications/filesystems.

%package     -n fuse-common
Summary:        Common files for File System in Userspace (FUSE) v2 and v3
License:        GPL-1.0-or-later

%description -n fuse-common
Common files for FUSE v2 and FUSE v3.

%prep
%autosetup -p1 -n fuse-%{version}

%conf -p
export LC_ALL=en_US.UTF-8

%install -a
find %{buildroot} .
# change from 4755 to 0755 to allow stripping -- fixed later in files
chmod 0755 %{buildroot}/%{_bindir}/fusermount3

# No need to create init-script
rm -f %{buildroot}%{_sysconfdir}/init.d/fuse3
# This path is hardcoded:
# https://github.com/libfuse/libfuse/blob/master/util/install_helper.sh#L43
# We also don't need this
rm -f %{buildroot}/etc/init.d/fuse3

# Install config-file
install -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}

# Delete pointless udev rules
rm -f %{buildroot}%{_udevrulesdir}/99-fuse3.rules

# Seems no check
%check

%files
%doc AUTHORS ChangeLog.rst README.md
%license LICENSE GPL2.txt
%{_sbindir}/mount.fuse3
%attr(4755,root,root) %{_bindir}/fusermount3
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_libdir}/libfuse3.so.*

%files devel
%{_libdir}/libfuse3.so
%{_libdir}/pkgconfig/fuse3.pc
%{_includedir}/fuse3/

%files -n fuse-common
%config(noreplace) %{_sysconfdir}/fuse.conf

%changelog
%autochangelog
