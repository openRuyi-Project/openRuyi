# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dracut
Version:        110
Release:        %autorelease
Summary:        Library to create ISO 9660 disk images
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://github.com/dracut-ng/dracut-ng
#!RemoteAsset:  sha256:0d357853f8cf2371d89a8ebcbbb1fd2c1c85a79d8866925fd7385eaeb20a27dc
Source:         %{url}/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --systemdsystemunitdir=%{_unitdir}
BuildOption(conf):  --bashcompletiondir=$(pkg-config --variable=completionsdir bash-completion)
BuildOption(conf):  --libdir=%{_prefix}/lib
BuildOption(conf):  --disable-dracut-cpio
BuildOption(conf):  --disable-documentation
# We can't run the whole test suite in the build environment
BuildOption(check):  TESTS="80 81"

BuildRequires:  bash
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  bash-completion
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libkmod)

Requires:       bash
Requires:       coreutils
Requires:       cpio
Requires:       filesystem
Requires:       findutils
Requires:       grep
Requires:       kmod
Requires:       sed
Requires:       zstd
Requires:       xz
Requires:       util-linux
Requires:       systemd
Requires:       systemd-udev
Requires:       iproute2

%description
dracut contains tools to create bootable initramfses for the Linux
kernel. Unlike other implementations, dracut hard-codes as little
as possible into the initramfs. dracut contains various modules which
are driven by the event-based udev. Having root on MD, DM, LVM2, LUKS
is supported as well as NFS, iSCSI, NBD, FCoE with the dracut-network
package.

%package        tools
Summary:        dracut tools to build the local initramfs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
This package contains tools to assemble the local initrd and host configuration.

%install -a
echo -e "#!/bin/bash\nDRACUT_VERSION=%{version}-%{release}" > %{buildroot}%{_prefix}/lib/dracut/dracut-version.sh

# No dash for now
rm -fr -- %{buildroot}%{_prefix}/lib/dracut/modules.d/10dash

# Remove architecture specific modules
rm -rf -- %{buildroot}%{_prefix}/lib/dracut/modules.d/68cms
rm -rf -- %{buildroot}%{_prefix}/lib/dracut/modules.d/69cio_ignore
rm -rf -- %{buildroot}%{_prefix}/lib/dracut/modules.d/73zipl
rm -rf -- %{buildroot}%{_prefix}/lib/dracut/modules.d/74dasd
rm -rf -- %{buildroot}%{_prefix}/lib/dracut/modules.d/74dasd_mod
rm -rf -- %{buildroot}%{_prefix}/lib/dracut/modules.d/74dcssblk
rm -rf -- %{buildroot}%{_prefix}/lib/dracut/modules.d/74zfcp
rm -rf -- %{buildroot}%{_prefix}/lib/dracut/modules.d/74znet

# We don't want example configs
rm -rf -- %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d

# We don't ship tests
rm -rf -- %{buildroot}%{_prefix}/lib/dracut/test
rm -rf -- %{buildroot}/%{_prefix}/lib/dracut/modules.d/80test*

mkdir -p %{buildroot}/boot/dracut
mkdir -p %{buildroot}/var/lib/dracut/overlay
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/dracut.log
mkdir -p %{buildroot}%{_sharedstatedir}/initramfs
mkdir -p %{buildroot}%{_prefix}/lib/dracutdracut.conf.d

rm -f %{buildroot}%{_mandir}/man?/*suse*

%files
%{_bindir}/dracut
%{_datadir}/bash-completion/completions/dracut
%{_datadir}/bash-completion/completions/lsinitrd
%{_bindir}/lsinitrd
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%{_prefix}/lib/dracut/dracut-functions.sh
%{_prefix}/lib/dracut/dracut-functions
%{_prefix}/lib/dracut/dracut-version.sh
%{_prefix}/lib/dracut/dracut-logger.sh
%{_prefix}/lib/dracut/dracut-initramfs-restore
%{_prefix}/lib/dracut/dracut-install
%{_prefix}/lib/dracut/dracut-util
%{_prefix}/lib/dracut/skipcpio
# %%{_prefix}/lib/dracut/dracut-cpio
%config(noreplace) %{_sysconfdir}/dracut.conf
%dir %{_sysconfdir}/dracut.conf.d
%dir %{_datadir}/pkgconfig
%{_datadir}/pkgconfig/dracut.pc
%{_prefix}/lib/dracut/modules.d/10bash
%{_prefix}/lib/dracut/modules.d/10systemd
%{_prefix}/lib/dracut/modules.d/10systemd-network-management
%{_prefix}/lib/dracut/modules.d/10warpclock
%{_prefix}/lib/dracut/modules.d/11fips
%{_prefix}/lib/dracut/modules.d/11fips-crypto-policies
%{_prefix}/lib/dracut/modules.d/11systemd-ac-power
%{_prefix}/lib/dracut/modules.d/11systemd-ask-password
%{_prefix}/lib/dracut/modules.d/11systemd-bsod
%{_prefix}/lib/dracut/modules.d/11systemd-battery-check
%{_prefix}/lib/dracut/modules.d/11systemd-coredump
%{_prefix}/lib/dracut/modules.d/11systemd-creds
%{_prefix}/lib/dracut/modules.d/11systemd-hostnamed
%{_prefix}/lib/dracut/modules.d/11systemd-initrd
%{_prefix}/lib/dracut/modules.d/11systemd-integritysetup
%{_prefix}/lib/dracut/modules.d/11systemd-journald
%{_prefix}/lib/dracut/modules.d/11systemd-ldconfig
%{_prefix}/lib/dracut/modules.d/11systemd-modules-load
%{_prefix}/lib/dracut/modules.d/11systemd-networkd
%{_prefix}/lib/dracut/modules.d/11systemd-pcrextend
%{_prefix}/lib/dracut/modules.d/11systemd-portabled
%{_prefix}/lib/dracut/modules.d/11systemd-pstore
%{_prefix}/lib/dracut/modules.d/11systemd-repart
%{_prefix}/lib/dracut/modules.d/11systemd-resolved
%{_prefix}/lib/dracut/modules.d/11systemd-sysext
%{_prefix}/lib/dracut/modules.d/11systemd-sysctl
%{_prefix}/lib/dracut/modules.d/11systemd-timedated
%{_prefix}/lib/dracut/modules.d/11systemd-timesyncd
%{_prefix}/lib/dracut/modules.d/11systemd-tmpfiles
%{_prefix}/lib/dracut/modules.d/11systemd-udevd
%{_prefix}/lib/dracut/modules.d/11systemd-veritysetup
%{_prefix}/lib/dracut/modules.d/12caps
%{_prefix}/lib/dracut/modules.d/13modsign
%{_prefix}/lib/dracut/modules.d/13rescue
%{_prefix}/lib/dracut/modules.d/14watchdog
%{_prefix}/lib/dracut/modules.d/14watchdog-modules
%{_prefix}/lib/dracut/modules.d/16dbus-broker
%{_prefix}/lib/dracut/modules.d/16dbus-daemon
%{_prefix}/lib/dracut/modules.d/16rngd
%{_prefix}/lib/dracut/modules.d/19dbus
%{_prefix}/lib/dracut/modules.d/20i18n
%{_prefix}/lib/dracut/modules.d/30convertfs
%{_prefix}/lib/dracut/modules.d/35connman
%{_prefix}/lib/dracut/modules.d/35network-manager
%{_prefix}/lib/dracut/modules.d/40network
%{_prefix}/lib/dracut/modules.d/45drm
%{_prefix}/lib/dracut/modules.d/45simpledrm
%{_prefix}/lib/dracut/modules.d/45net-lib
%{_prefix}/lib/dracut/modules.d/45plymouth
%{_prefix}/lib/dracut/modules.d/45systemd-import
%{_prefix}/lib/dracut/modules.d/45url-lib
%{_prefix}/lib/dracut/modules.d/68lvmmerge
%{_prefix}/lib/dracut/modules.d/68lvmthinpool-monitor
%{_prefix}/lib/dracut/modules.d/70bluetooth
%{_prefix}/lib/dracut/modules.d/70btrfs
%{_prefix}/lib/dracut/modules.d/70crypt
%{_prefix}/lib/dracut/modules.d/70dm
%{_prefix}/lib/dracut/modules.d/70dmraid
%{_prefix}/lib/dracut/modules.d/70dmsquash-live
%{_prefix}/lib/dracut/modules.d/70dmsquash-live-autooverlay
%{_prefix}/lib/dracut/modules.d/70dmsquash-live-ntfs
%{_prefix}/lib/dracut/modules.d/70fs-lib
%{_prefix}/lib/dracut/modules.d/70img-lib
%{_prefix}/lib/dracut/modules.d/70kernel-modules
%{_prefix}/lib/dracut/modules.d/70kernel-modules-export
%{_prefix}/lib/dracut/modules.d/70kernel-modules-extra
%{_prefix}/lib/dracut/modules.d/70kernel-network-modules
%{_prefix}/lib/dracut/modules.d/70livenet
%{_prefix}/lib/dracut/modules.d/70lvm
%{_prefix}/lib/dracut/modules.d/70mdraid
%{_prefix}/lib/dracut/modules.d/70memdisk
%{_prefix}/lib/dracut/modules.d/70multipath
%{_prefix}/lib/dracut/modules.d/70nvdimm
%{_prefix}/lib/dracut/modules.d/70numlock
%{_prefix}/lib/dracut/modules.d/70overlayfs
%{_prefix}/lib/dracut/modules.d/70ppcmac
%{_prefix}/lib/dracut/modules.d/70pcmcia
%{_prefix}/lib/dracut/modules.d/70qemu
%{_prefix}/lib/dracut/modules.d/70qemu-net
%{_prefix}/lib/dracut/modules.d/70uefi-lib
%{_prefix}/lib/dracut/modules.d/71systemd-cryptsetup
%{_prefix}/lib/dracut/modules.d/73crypt-gpg
%{_prefix}/lib/dracut/modules.d/73crypt-loop
%{_prefix}/lib/dracut/modules.d/73fido2
%{_prefix}/lib/dracut/modules.d/73pcsc
%{_prefix}/lib/dracut/modules.d/73pkcs11
%{_prefix}/lib/dracut/modules.d/73tpm2-tss
%{_prefix}/lib/dracut/modules.d/74debug
%{_prefix}/lib/dracut/modules.d/74cifs
%{_prefix}/lib/dracut/modules.d/74fcoe
%{_prefix}/lib/dracut/modules.d/74fcoe-uefi
%{_prefix}/lib/dracut/modules.d/74fstab-sys
%{_prefix}/lib/dracut/modules.d/74hwdb
%{_prefix}/lib/dracut/modules.d/74iscsi
%{_prefix}/lib/dracut/modules.d/74lunmask
%{_prefix}/lib/dracut/modules.d/74nbd
%{_prefix}/lib/dracut/modules.d/74nfs
%{_prefix}/lib/dracut/modules.d/74nvmf
%{_prefix}/lib/dracut/modules.d/74resume
%{_prefix}/lib/dracut/modules.d/74rootfs-block
%{_prefix}/lib/dracut/modules.d/74rootfs-block-fallback
%{_prefix}/lib/dracut/modules.d/74ssh-client
%{_prefix}/lib/dracut/modules.d/74squash-erofs
%{_prefix}/lib/dracut/modules.d/74squash-squashfs
%{_prefix}/lib/dracut/modules.d/74terminfo
%{_prefix}/lib/dracut/modules.d/74udev-rules
%{_prefix}/lib/dracut/modules.d/74virtfs
%{_prefix}/lib/dracut/modules.d/74virtiofs
%{_prefix}/lib/dracut/modules.d/75securityfs
%{_prefix}/lib/dracut/modules.d/76masterkey
%{_prefix}/lib/dracut/modules.d/77integrity
%{_prefix}/lib/dracut/modules.d/76biosdevname
%{_prefix}/lib/dracut/modules.d/76systemd-emergency
%{_prefix}/lib/dracut/modules.d/77dracut-systemd
%{_prefix}/lib/dracut/modules.d/77ecryptfs
%{_prefix}/lib/dracut/modules.d/77pollcdrom
%{_prefix}/lib/dracut/modules.d/77selinux
%{_prefix}/lib/dracut/modules.d/77syslog
%{_prefix}/lib/dracut/modules.d/77usrmount
%{_prefix}/lib/dracut/modules.d/77initqueue
%{_prefix}/lib/dracut/modules.d/78systemd-sysusers
%{_prefix}/lib/dracut/modules.d/80base
%{_prefix}/lib/dracut/modules.d/81busybox
%{_prefix}/lib/dracut/modules.d/84memstrack
%{_prefix}/lib/dracut/modules.d/85shell-interpreter
%{_prefix}/lib/dracut/modules.d/86shutdown
%{_prefix}/lib/dracut/modules.d/87squash
%{_prefix}/lib/dracut/modules.d/88squash-lib
#{_prefix}/lib/dracut/modules.d/99openssl
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/log/dracut.log
%dir %{_sharedstatedir}/initramfs
%{_unitdir}/dracut-shutdown.service
%{_unitdir}/dracut-shutdown-onfailure.service
%{_unitdir}/sysinit.target.wants/dracut-shutdown.service
%{_unitdir}/dracut-cmdline.service
%{_unitdir}/dracut-initqueue.service
%{_unitdir}/dracut-mount.service
%{_unitdir}/dracut-pre-mount.service
%{_unitdir}/dracut-pre-pivot.service
%{_unitdir}/dracut-pre-trigger.service
%{_unitdir}/dracut-pre-udev.service
%{_unitdir}/initrd.target.wants/dracut-cmdline.service
%{_unitdir}/initrd.target.wants/dracut-initqueue.service
%{_unitdir}/initrd.target.wants/dracut-mount.service
%{_unitdir}/initrd.target.wants/dracut-pre-mount.service
%{_unitdir}/initrd.target.wants/dracut-pre-pivot.service
%{_unitdir}/initrd.target.wants/dracut-pre-trigger.service
%{_unitdir}/initrd.target.wants/dracut-pre-udev.service
%{_prefix}/lib/kernel/install.d/50-dracut.install
%{_prefix}/lib/kernel/install.d/51-dracut-rescue.install

%files tools
%{_bindir}/dracut-catimages
%dir /boot/dracut
%dir %{_localstatedir}/lib/dracut
%dir %{_localstatedir}/lib/dracut/overlay

%changelog
%autochangelog
