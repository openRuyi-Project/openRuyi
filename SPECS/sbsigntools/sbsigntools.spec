# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xiang W <wangxiang@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sbsigntools
Version:        0.9.5
Release:        %autorelease
Summary:        Signing utility for UEFI secure boot
License:        GPL-3.0-only
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git
#!RemoteAsset:  sha256:a2323e54be6d17f50ceb3253ca6ed063171a5bcb7079bfa594008cd2aeb7fdea
Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git/snapshot/sbsigntools-0.9.5.tar.gz
# source1 is submodule at lib/ccan.git
#!RemoteAsset:  sha256:d479cffd70764aa6078d7b198472a9ec0b517b2123479fb578b3e5c8ddaa01b0
Source1:        https://github.com/rustyrussell/ccan/archive/b1f28e17227f2320d07fe052a8a48942fe17caa5.tar.gz
BuildSystem:    autotools

# Fix the following compile-time errors
# [   13s] gcc -Wall -Wextra --std=gnu99 -DOPENSSL_API_COMPAT=0x10100000L -I../lib/ccan/ -Werror -O2 -g -fno-omit-frame-pointer -pipe -flto=auto -ffat-lto-objects -funwind-tables -fasynchronous-unwind-tables -fstack-protector-strong -D_FORTIFY_SOURCE=3 -fstack-clash-protection -Wformat -Werror=format-security  -Wl,-z,relro,-z,now,-z,noexecstack -o sbkeysync sbkeysync-sbkeysync.o sbkeysync-idc.o sbkeysync-image.o sbkeysync-fileio.o  ../lib/ccan/libccan.a -lcrypto -luuid
# [   13s] In function ‘_talloc_set_name_const’,
# [   13s]     inlined from ‘_talloc_named_const’ at ../lib/ccan/ccan/talloc/talloc.c:352:2,
# [   13s]     inlined from ‘_talloc_zero’ at ../lib/ccan/ccan/talloc/talloc.c:1270:6,
# [   13s]     inlined from ‘main’ at sbkeysync.c:895:8:
# [   13s] ../lib/ccan/ccan/talloc/talloc.c:336:35: error: ‘_169’ may be used uninitialized [-Werror=maybe-uninitialized]
# [   13s]   336 |         struct talloc_chunk *tc = talloc_chunk_from_ptr(ptr);
# [   13s]       |                                   ^
# [   13s] ../lib/ccan/ccan/talloc/talloc.c: In function ‘main’:
# [   13s] ../lib/ccan/ccan/talloc/talloc.c:115:36: note: by argument 1 of type ‘const void *’ to ‘talloc_chunk_from_ptr’ declared here
# [   13s]   115 | static inline struct talloc_chunk *talloc_chunk_from_ptr(const void *ptr)
# [   13s]       |                                    ^
# [   13s] lto1: all warnings being treated as errors
# [   13s] make[3]: *** [/tmp/ccivTu4P.mk:2: /tmp/ccCeK3QL.ltrans0.ltrans.o] Error 1
# [   13s] lto-wrapper: fatal error: make returned 2 exit status
# [   13s] compilation terminated.
Patch2000:      2000-fix-lto-uninitialized.diff

BuildOption(build):  LD=ld.bfd

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  binutils-devel
BuildRequires:  gnu-efi
BuildRequires:  help2man
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(uuid)

%description
Signing utility for UEFI secure boot

%prep -a
tar --strip-components=1 -xf %{SOURCE1} -C lib/ccan.git

%conf -p
./autogen.sh

%check
# No tests

%files
%doc README AUTHORS ChangeLog
%license LICENSE.GPLv3
%{_bindir}/sbkeysync
%{_bindir}/sbsiglist
%{_bindir}/sbvarsign
%{_bindir}/sbattach
%{_bindir}/sbverify
%{_bindir}/sbsign
%{_mandir}/man1/sbkeysync.1.gz
%{_mandir}/man1/sbsiglist.1.gz
%{_mandir}/man1/sbvarsign.1.gz
%{_mandir}/man1/sbattach.1.gz
%{_mandir}/man1/sbverify.1.gz
%{_mandir}/man1/sbsign.1.gz

%changelog
%autochangelog
