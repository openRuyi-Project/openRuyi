# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: avrovadonz2026 <jinyuan.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mdevd
Version:        0.1.8.1
Release:        %autorelease
Summary:        A mdev-compatible Linux hotplug manager daemon
License:        ISC
URL:            https://skarnet.org/software/mdevd/
VCS:            git:https://github.com/skarnet/mdevd
#!RemoteAsset:  sha256:93d2bba7299ff3b1b9f249928c2e84e23a5af3d829ebd9677ea44535c585aa82
Source0:        %{url}/mdevd-%{version}.tar.gz
BuildSystem:    autotools

# from https://github.com/skarnet/mdevd/commit/4594ed03e4ced04cb914c8fccad1ffab41cc4ee5
Patch0:         some-libcs-have-a-char-const-strchr-need-to-investigate.patch

BuildOption(conf):  --with-pkgconfig
BuildOption(conf):  --with-sysdeps=%{_libdir}/skalibs/sysdeps
BuildOption(conf):  --disable-allstatic

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  skalibs-devel

%description
mdevd is a small daemon managing Linux kernel hotplug events, similarly
to udevd. It is designed as a drop-in replacement for BusyBox mdev that
listens on netlink instead of forking a new process for every event.

%install -a
# Upstream always installs a generated config header even though mdevd
# does not expose a public development interface.
rm -rf %{buildroot}%{_includedir}/%{name}

%check
# No upstream test target is provided.

%files
%license COPYING
%doc AUTHORS CONTRIBUTING DCO INSTALL NEWS README
%doc doc/*.html
%doc examples/
%doc src/mdevd/PARSING.txt
%{_bindir}/mdevd
%{_bindir}/mdevd-coldplug

%changelog
%autochangelog
