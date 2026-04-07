# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rpmdevtools
Version:        9.6
Release:        %autorelease
Summary:        RPM Development Tools
# rpmdev-md5 and rpmdev-setuptree are GPL-2.0-only,
# everything else is GPL-2.0-or-later.
License:        GPL-2.0-or-later AND GPL-2.0-only
URL:            https://pagure.io/rpmdevtools
VCS:            git:https://pagure.io/rpmdevtools.git
#!RemoteAsset:  sha256:794c97afeb6e81867497b84d2ecfd42dc8c984f59fbab8282f5396419ca7cb9e
Source:         https://releases.pagure.org/rpmdevtools/rpmdevtools-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --libdir=%{_prefix}/lib

BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  help2man
BuildRequires:  perl
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(rpm)
BuildRequires:  python3dist(progressbar2)
BuildRequires:  pkgconfig(python)

Requires:       curl
Requires:       diffutils
Requires:       fakeroot
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       rpm-build
Requires:       python3dist(argcomplete)
Requires:       python3dist(requests)
Requires:       python3dist(rpm)
Requires:       sed
Requires:       python3dist(progressbar2)

Recommends:     python3dist(rpmautospec)

%description
This package contains scripts and (X)Emacs support files to aid in
development of RPM packages.
rpmdev-setuptree    Create RPM build tree within user's home directory
rpmdev-diff         Diff contents of two archives
rpmdev-newspec      Creates new .spec from template
rpmdev-rmdevelrpms  Find (and optionally remove) "development" RPMs
rpmdev-checksig     Check package signatures using alternate RPM keyring
rpminfo             Print information about executables and libraries
rpmdev-md5/sha*     Display checksums of all files in an archive file
rpmdev-vercmp       RPM version comparison checker
rpmdev-spectool     Expand and download sources and patches in specfiles
rpmdev-wipetree     Erase all files within dirs created by rpmdev-setuptree
rpmdev-extract      Extract various archives, "tar xvf" style
rpmdev-bumpspec     Bump revision in specfile
...and many more.

%prep -a
grep -lF "%{_bindir}/python " * | xargs sed -i -e "s|%{_bindir}/python |%{_bindir}/python3 |"

# No tests
%check

%files
%license COPYING
%doc NEWS
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/rpmdevtools/
%{_datadir}/rpmdevtools/
%{_datadir}/bash-completion/completions/*
%{_mandir}/man[18]/*.[18]*

%changelog
%autochangelog
