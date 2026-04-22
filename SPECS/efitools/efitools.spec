# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           efitools
Version:        1.9.2
Release:        %autorelease
Summary:        useful tools for manipulating UEFI secure boot platforms
License:        GPL-2.0-only AND LGPL-2.1-only AND BSD-2-Clause
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
VCS:            git:https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
#!RemoteAsset:  sha256:0f315b36e7d1ba74bfc97ab9f304f0a3072c47578bbe5e42594acae381f9acfe
Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git/snapshot/efitools-%{version}.tar.gz
BuildSystem:    autotools

# fix building error
Patch2000:      2000-fix-build-error.diff

BuildOption(build):  LD=ld.bfd
BuildOption(install):  DESTDIR=%{buildroot}

BuildRequires:  gnu-efi
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  perl
BuildRequires:  perl-File-Slurp
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  sbsigntools

%description
useful tools for manipulating UEFI secure boot platforms

# No configure
%conf

# No tests
%check

%files
%doc README
%license COPYING
%{_bindir}/cert-to-efi-hash-list
%{_bindir}/cert-to-efi-sig-list
%{_bindir}/efi-readvar
%{_bindir}/efitool-mkusb
%{_bindir}/efi-updatevar
%{_bindir}/flash-var
%{_bindir}/hash-to-efi-sig-list
%{_bindir}/sig-list-to-certs
%{_bindir}/sign-efi-sig-list
%{_datadir}/%{name}/COPYING
%{_datadir}/%{name}/efi/HashTool.efi
%{_datadir}/%{name}/efi/HelloWorld.efi
%{_datadir}/%{name}/efi/KeyTool.efi
%{_datadir}/%{name}/efi/Loader.efi
%{_datadir}/%{name}/efi/LockDown.efi
%{_datadir}/%{name}/efi/ReadVars.efi
%{_datadir}/%{name}/efi/SetNull.efi
%{_datadir}/%{name}/efi/ShimReplace.efi
%{_datadir}/%{name}/efi/UpdateVars.efi
%{_datadir}/%{name}/README
%{_mandir}/man1/cert-to-efi-hash-list.1.gz
%{_mandir}/man1/cert-to-efi-sig-list.1.gz
%{_mandir}/man1/efi-readvar.1.gz
%{_mandir}/man1/efi-updatevar.1.gz
%{_mandir}/man1/hash-to-efi-sig-list.1.gz
%{_mandir}/man1/sig-list-to-certs.1.gz
%{_mandir}/man1/sign-efi-sig-list.1.gz

%changelog
%autochangelog
