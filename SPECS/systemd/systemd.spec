# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# We ship a .pc file but don't want to have a dep on pkg-config. We
# strip the automatically generated dep here and instead co-own the
# directory.
%global __requires_exclude pkg-config

%global pkgdir %{_prefix}/lib/systemd
%global system_unit_dir %{pkgdir}/system
%global user_unit_dir %{pkgdir}/user

# If we want to enable bootstrap, change this to 1
# When bootstrap, libcryptsetup is disabled
# but auto-features causes many options to be turned on
# that depend on libcryptsetup (e.g. libcryptsetup-plugins, homed)
%bcond bootstrap 1
%if %{with bootstrap}
%global __meson_auto_features disabled
%endif
# TODO: We disable lots of stuff so if we want to enable them
#.      Please first check the spec file. Thanks. - 251
# If we want systemd-journal-remote, change this to 1
%bcond journal_remote 0
# If we have X then we can build systemd with X support
%bcond x 0
# If we want network support, change this to 1
%bcond network 1
# If we want FIDO2 key support, change this to 1
%bcond fido2 0
# I don't think we ever want to enable TPM2 support
%bcond tpm2 0
# Sorry, no docs yet
%bcond docs 0
# If we want to Unified Kernel Image then change this
%bcond ukify 1
# We don't want to run valgrind tests in CI
# Or we just don't want tests at all
%bcond valgrind 0
# We don't want eBPF support yet
%bcond bpf 0

%global base_version 257

Name:           systemd
Version:        %{base_version}.9
Release:        %autorelease
Summary:        System and service manager
License:        LGPL-2.1-or-later AND MIT AND GPL-2.0-or-later
URL:            https://systemd.io
#!RemoteAsset
Source0:        https://github.com/systemd/systemd/archive/v%{version}/%{name}-%{version}.tar.gz
# These are essential files
Source1:        systemd-user
BuildSystem:    meson

BuildOption(conf):  -Dmode=release
BuildOption(conf):  -Dsbat-distro-url='%{_vendor_url}'
BuildOption(conf):  -Drc-local=/etc/rc.d/rc.local
BuildOption(conf):  -Ddns-servers=''
BuildOption(conf):  -Dkmod=enabled
BuildOption(conf):  -Dxkbcommon=%{?with_x:enabled}%{!?with_x:disabled}
BuildOption(conf):  -Dselinux=disabled
BuildOption(conf):  -Dbpf-framework=%{?with_bpf:enabled}%{!?with_bpf:disabled}
BuildOption(conf):  -Dvmlinux-h=disabled
#BuildOption(conf):  -Dvmlinux-h-path="$VMLINUX_H_PATH"
BuildOption(conf):  -Dapparmor=disabled
BuildOption(conf):  -Dxz=enabled
BuildOption(conf):  -Dzlib=enabled
BuildOption(conf):  -Dbzip2=enabled
BuildOption(conf):  -Dlz4=enabled
BuildOption(conf):  -Dzstd=enabled
BuildOption(conf):  -Dpam=enabled
BuildOption(conf):  -Dacl=enabled
BuildOption(conf):  -Dsmack=false
BuildOption(conf):  -Dblkid=enabled
BuildOption(conf):  -Dopenssl=enabled
BuildOption(conf):  -Dp11kit=%{?with_bootstrap:disabled}%{!?with_bootstrap:enabled}
BuildOption(conf):  -Dgcrypt=disabled
BuildOption(conf):  -Delfutils=enabled
BuildOption(conf):  -Dlibcryptsetup=%{?with_bootstrap:disabled}%{!?with_bootstrap:enabled}
BuildOption(conf):  -Drepart=enabled
BuildOption(conf):  -Dpwquality=enabled
BuildOption(conf):  -Dqrencode=disabled
BuildOption(conf):  -Dgnutls=enabled
BuildOption(conf):  -Dmicrohttpd=%{?with_journal_remote:enabled}%{!?with_journal_remote:disabled}
BuildOption(conf):  -Dvmspawn=%{?with_bootstrap:disabled}%{!?with_bootstrap:enabled}
BuildOption(conf):  -Dlibidn2=enabled
BuildOption(conf):  -Dlibiptc=%{?with_network:enabled}%{!?with_network:disabled}
BuildOption(conf):  -Dnetworkd=%{?with_network:true}%{!?with_network:false}
BuildOption(conf):  -Dresolve=%{?with_network:true}%{!?with_network:false}
BuildOption(conf):  -Dnss-resolve=%{?with_network:enabled}%{!?with_network:disabled}
BuildOption(conf):  -Dlibcurl=enabled
BuildOption(conf):  -Dlibfido2=%{?with_fido2:enabled}%{!?with_fido2:disabled}
BuildOption(conf):  -Defi=true
BuildOption(conf):  -Dbootloader=enabled
BuildOption(conf):  -Dtpm2=%{?with_tpm2:enabled}%{!?with_tpm2:disabled}
BuildOption(conf):  -Dukify=%{?with_ukify:enabled}%{!?with_ukify:disabled}
BuildOption(conf):  -Dhwdb=true
BuildOption(conf):  -Dsysusers=true
# Enable only if we really want it
BuildOption(conf):  -Dstandalone-binaries=false
BuildOption(conf):  -Ddefault-kill-user-processes=false
BuildOption(conf):  -Dfirst-boot-full-preset=true
# No Tests
BuildOption(conf):  -Dtests=false
BuildOption(conf):  -Dinstall-tests=false
BuildOption(conf):  -Dnobody-user=nobody
BuildOption(conf):  -Dnobody-group=nobody
BuildOption(conf):  -Dman=%{?with_docs:enabled}%{!?with_docs:disabled}
BuildOption(conf):  -Dfallback-hostname="localhost"
BuildOption(conf):  -Ddefault-dnssec=no
BuildOption(conf):  -Ddefault-dns-over-tls=no
BuildOption(conf):  -Ddefault-mdns=no
BuildOption(conf):  -Ddefault-timeout-sec=45
BuildOption(conf):  -Ddefault-user-timeout-sec=45
BuildOption(conf):  -Dconfigfiledir=/usr/lib
BuildOption(conf):  -Doomd=true
BuildOption(conf):  -Dtty-gid=5
# If we have this then we can have BuildRequires: gettext.
BuildOption(conf):  -Dtranslations=false
BuildOption(conf):  -Dfdisk=enabled
BuildOption(conf):  -Dsysupdate=enabled

#BuildRequires:  clang
BuildRequires:  coreutils
BuildRequires:  libcap-devel
BuildRequires:  util-linux-devel
BuildRequires:  libpwquality-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  pam-devel
BuildRequires:  libselinux-devel
BuildRequires:  audit-devel
%if %{without bootstrap}
BuildRequires:  cryptsetup-devel
%endif
BuildRequires:  dbus-devel
BuildRequires:  acl-devel
BuildRequires:  libblkid
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  lz4-devel
BuildRequires:  lz4
BuildRequires:  bzip2-devel
BuildRequires:  zstd-devel
BuildRequires:  libidn2-devel
BuildRequires:  libcurl-devel
BuildRequires:  kmod-devel
BuildRequires:  openssl-devel
BuildRequires:  gnutls-devel
BuildRequires:  p11-kit-devel
BuildRequires:  libdw-devel
%if %{with journal_remote}
BuildRequires:  libmicrohttpd-devel
%endif
%if %{with x}
# Used by systemd-localed & systemd-firstboot
BuildRequires:  libxkbcommon-devel
%endif
%if %{with network}
BuildRequires:  iptables-legacy-devel
%endif
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libarchive)
%if %{with fido2}
BuildRequires:  libfido2-devel
%endif
%if %{with tpm2}
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(tss2-rc)
BuildRequires:  pkgconfig(tss2-mu)
%endif
BuildRequires:  python3
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(lxml)
%if %{with docs}
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
%endif
BuildRequires:  pkgconfig
BuildRequires:  gperf
BuildRequires:  gawk
%if %{with ukify}
BuildRequires:  python3dist(pefile)
# BuildRequires:  python3dist(pillow)
%endif
BuildRequires:  python3dist(pyelftools)
BuildRequires:  libseccomp-devel
BuildRequires:  meson
%if %{with valgrind}
BuildRequires:  valgrind-devel
%endif
%if %{with bpf}
BuildRequires:  bpftool
BuildRequires:  pkgconfig(libbpf)
%endif

BuildRequires:  distribution-release

Requires:       dbus
Requires(post): coreutils
Requires(post): grep
# systemd-machine-id-setup requires libssl
Requires(post): openssl
Requires:       %{name}-pam = %{version}-%{release}
Requires(meta): (%{name}-rpm-macros = %{version}-%{release} if rpm-build)
Requires:       %{name}-libs = %{version}-%{release}

Provides:       systemd = %{version}-%{release}
Provides:       %{_bindir}/systemctl
Provides:       %{_bindir}/shutdown
Provides:       syslog
Provides:       systemd-units = %{version}-%{release}

%description
systemd is a system and service manager that runs as PID 1 and starts the rest
of the system. It provides aggressive parallelization capabilities, uses socket
and D-Bus activation for starting services, offers on-demand starting of
daemons, keeps track of processes using Linux control groups, maintains mount
and automount points, and implements an elaborate transactional dependency-based
service control logic. systemd supports SysV and LSB init scripts and works as a
replacement for sysvinit. Other parts of this package are a logging daemon,
utilities to control basic system configuration like the hostname, date, locale,
maintain a list of logged-in users, system accounts, runtime directories and
settings, and a logging daemons.

%package        libs
Summary:        systemd libraries
License:        LGPL-2.1-or-later AND MIT
Provides:       nss-myhostname = 0.4

%description    libs
Libraries for systemd and udev.

%package        shared
Summary:        Internal systemd shared library
License:        LGPL-2.1-or-later AND MIT

%description    shared
Internal libraries used by various systemd binaries.

%package        pam
Summary:        systemd PAM module

%description    pam
Systemd PAM module registers the session with systemd-logind.

%package        rpm-macros
Summary:        Macros that define paths and scriptlets related to systemd
BuildArch:      noarch

%description    rpm-macros
Just the definitions of rpm macros.

%package        sysusers
Summary:        systemd-sysusers program
Requires:       %{name}-shared = %{version}-%{release}

%description    sysusers
This package contains the systemd-sysusers program.

%package        devel
Summary:        Development headers for systemd
License:        LGPL-2.1-or-later AND MIT
Requires:       %{name}-libs = %{version}-%{release}
Requires:       kmod-devel
Requires:       libidn2-devel
Requires(meta): (%{name}-rpm-macros = %{version}-%{release} if rpm-build)
Provides:       libudev-devel = %{version}

%description    devel
Development headers and auxiliary files for developing applications linking
to libudev or libsystemd.

%package        udev
Summary:        Rule-based device node and kernel event manager
License:        LGPL-2.1-or-later
Requires:       systemd = %{version}-%{release}
Requires(post):   systemd = %{version}-%{release}
Requires(preun):  systemd = %{version}-%{release}
Requires(postun): systemd = %{version}-%{release}
Requires(post): grep
Provides:       udev = %{version}
Provides:       systemd-timesyncd = %{version}-%{release}
Requires:       kbd

%description udev
This package contains systemd-udev and the rules and hardware database needed to
manage device nodes. This package is necessary on physical machines and in
virtual machines, but not in containers.

This package also provides systemd-timesyncd, a network time protocol daemon.

It also contains tools to manage encrypted home areas and secrets bound to the
machine, and to create or grow partitions and make file systems automatically.

%if %{with ukify}
%package        ukify
Summary:        Tool to build Unified Kernel Images
BuildRequires:  binutils
Requires:       %{name} = %{version}-%{release}
Requires:       systemd-boot
Requires:       python3dist(pefile)
Recommends:     python3dist(zstandard)
Requires:       python3dist(cryptography)
Recommends:     python3dist(pillow)
BuildArch:      noarch

%description    ukify
This package provides ukify, a script that combines a kernel image, an initrd,
with a command line, and possibly PCR measurements and other metadata, into a
Unified Kernel Image (UKI).
%endif

%package        boot
Summary:        UEFI boot manager
Provides:       systemd-boot = %{version}-%{release}

%description    boot
systemd-boot (short: sd-boot) is a simple UEFI boot manager. It provides a
graphical menu to select the entry to boot and an editor for the kernel command
line. systemd-boot supports systems with UEFI firmware only

%package        container
Summary:        Tools for containers and VMs
Requires:       %{name} = %{version}-%{release}
Requires(post):   systemd = %{version}-%{release}
Requires(preun):  systemd = %{version}-%{release}
Requires(postun): systemd = %{version}-%{release}
License:        LGPL-2.1-or-later

%description    container
Systemd tools to spawn and manage containers and virtual machines.

This package contains systemd-nspawn, systemd-vmspawn, machinectl,
systemd-machined, and systemd-importd.

%if %{with journal_remote}
%package        journal-remote
Summary:        Tools to send journal events over the network
Requires:       %{name} = %{version}-%{release}
License:        LGPL-2.1-or-later
Provides:       %{name}-journal-gateway = %{version}-%{release}
Provides:       %{name}-journal-gateway = %{version}-%{release}

%description    journal-remote
Programs to forward journal entries over the network, using encrypted HTTP, and
to write journal files from serialized journal contents.

This package contains systemd-journal-gatewayd, systemd-journal-remote, and
systemd-journal-upload.
%endif

%if %{with network}
%package        networkd
Summary:        System daemon that manages network configurations
Requires:       %{name} = %{version}-%{release}
Recommends:     %{name}-udev = %{version}-%{release}
License:        LGPL-2.1-or-later

%description    networkd
systemd-networkd is a system service that manages networks. It detects and
configures network devices as they appear, as well as creating virtual network
devices.

%package        networkd-defaults
Summary:        Configure network interfaces with networkd by default
Requires:       %{name}-networkd = %{version}-%{release}
License:        MIT-0
BuildArch:      noarch

%description    networkd-defaults
This package contains a set of config files for systemd-networkd that cause it
to configure network interfaces by default. Note that systemd-networkd needs to
enabled for this to have any effect.

%package        resolved
Summary:        Network Name Resolution manager
Requires:       %{name} = %{version}-%{release}
Requires(posttrans): grep

%description    resolved
systemd-resolved is a system service that provides network name resolution to
local applications. It implements a caching and validating DNS/DNSSEC stub
resolver, as well as an LLMNR and MulticastDNS resolver and responder.
%endif

%package        oomd-defaults
Summary:        Configuration files for systemd-oomd
Requires:       %{name}-udev = %{version}-%{release}
License:        LGPL-2.1-or-later
BuildArch:      noarch

%description    oomd-defaults
A set of drop-in files for systemd units to enable action from systemd-oomd,
a userspace out-of-memory (OOM) killer.

%package        repart
Summary:        systemd-repart

%description    repart
This package provide systemd-repart.

%package        dissect
Summary:        systemd-dissect

%description    dissect
This package provide mount.ddi and systemd-dissect.

%package     -n kernel-install
Summary:        This package provides kernel-install tool

%description -n kernel-install
This package provides kernel-install tool

%prep -a
%if %{with bpf}
%global find_vmlinux_h %{expand:
import functools, glob, subprocess
def cmp(a, b):
  c = subprocess.call(["rpmdev-vercmp", a, b], stdout=subprocess.DEVNULL)
  return {0:0, 11:+1, 12:-1}[c]
choices = list(glob.glob("/usr/src/kernels/*/vmlinux.h"))
assert choices
print(max(choices, key=functools.cmp_to_key(cmp)))
}

VMLINUX_H_PATH=$(%python3 -c '%find_vmlinux_h')
%endif

%build -a
# Dynamic spec generation is available for us
cp %{_vpath_builddir}/src/rpm/triggers.systemd.sh %{specpartsdir}/triggers.specpart

%install -a
# Compatiblity and documentation files
touch %{buildroot}/etc/crypttab
chmod 600 %{buildroot}/etc/crypttab

# Config files that were moved under /usr.
# We need to %ghost them so that they are not removed on upgrades.
touch %{buildroot}/etc/systemd/coredump.conf \
      %{buildroot}/etc/systemd/homed.conf \
      %{buildroot}/etc/systemd/journald.conf \
      %{buildroot}/etc/systemd/journal-remote.conf \
      %{buildroot}/etc/systemd/journal-upload.conf \
      %{buildroot}/etc/systemd/logind.conf \
      %{buildroot}/etc/systemd/networkd.conf \
      %{buildroot}/etc/systemd/oomd.conf \
      %{buildroot}/etc/systemd/pstore.conf \
      %{buildroot}/etc/systemd/resolved.conf \
      %{buildroot}/etc/systemd/sleep.conf \
      %{buildroot}/etc/systemd/system.conf \
      %{buildroot}/etc/systemd/timesyncd.conf \
      %{buildroot}/etc/systemd/user.conf \
      %{buildroot}/etc/udev/udev.conf \
      %{buildroot}/etc/udev/iocost.conf

# Since v207 /etc/sysctl.conf is no longer parsed (commit 04bf3c1a60d82791),
# however backward compatibility is provided by the following symlink.
ln -s ../sysctl.conf %{buildroot}/etc/sysctl.d/99-sysctl.conf
touch %{buildroot}%{_sysconfdir}/sysctl.conf

# Make sure these directories are properly owned
mkdir -p %{buildroot}%{system_unit_dir}/basic.target.wants
mkdir -p %{buildroot}%{system_unit_dir}/default.target.wants
mkdir -p %{buildroot}%{system_unit_dir}/dbus.target.wants
mkdir -p %{buildroot}%{system_unit_dir}/syslog.target.wants
mkdir -p %{buildroot}/run
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/lastlog
chmod 0664 %{buildroot}%{_localstatedir}/log/lastlog
touch %{buildroot}/run/utmp
touch %{buildroot}%{_localstatedir}/log/{w,b}tmp

# Make sure the user generators dir exists too
mkdir -p %{buildroot}%{pkgdir}/system-generators
mkdir -p %{buildroot}%{pkgdir}/user-generators

# Create new-style configuration files so that we can ghost-own them
touch %{buildroot}%{_sysconfdir}/hostname
touch %{buildroot}%{_sysconfdir}/vconsole.conf
touch %{buildroot}%{_sysconfdir}/locale.conf
touch %{buildroot}%{_sysconfdir}/machine-id
touch %{buildroot}%{_sysconfdir}/machine-info
touch %{buildroot}%{_sysconfdir}/localtime
mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d
touch %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf

# Make sure the shutdown/sleep drop-in dirs exist
mkdir -p %{buildroot}%{pkgdir}/system-shutdown/
mkdir -p %{buildroot}%{pkgdir}/system-sleep/

# Make sure directories in /var exist
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/coredump
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/catalog
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/backlight
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/rfkill
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/linger
mkdir -p %{buildroot}%{_localstatedir}/lib/private
mkdir -p %{buildroot}%{_localstatedir}/log/private
mkdir -p %{buildroot}%{_localstatedir}/cache/private
mkdir -p %{buildroot}%{_localstatedir}/lib/private/systemd/journal-upload
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/timesync
ln -s ../private/systemd/journal-upload %{buildroot}%{_localstatedir}/lib/systemd/journal-upload
mkdir -p %{buildroot}%{_localstatedir}/log/journal
touch %{buildroot}%{_localstatedir}/lib/systemd/catalog/database
touch %{buildroot}%{_sysconfdir}/udev/hwdb.bin
touch %{buildroot}%{_localstatedir}/lib/systemd/random-seed
touch %{buildroot}%{_localstatedir}/lib/systemd/timesync/clock
%if %{with journal_remote}
touch %{buildroot}%{_localstatedir}/lib/private/systemd/journal-upload/state
%endif

install -m 0644 -t %{buildroot}%{_prefix}/lib/pam.d/ %{SOURCE1}

# Remove unwanted README
rm -f %{buildroot}%{_sysconfdir}/init.d/README
# Disable sshd_config.d/20-systemd-userdb.conf
# See https://github.com/systemd/systemd/issues/33648
rm %{buildroot}/etc/ssh/sshd_config.d/20-systemd-userdb.conf
mv %{buildroot}/usr/lib/tmpfiles.d/20-systemd-userdb.conf{,.example}

%post
systemd-machine-id-setup &>/dev/null || :

[ $1 -eq 1 ] || exit 0

# create /var/log/journal only on initial installation,
# and only if it's writable (it won't be in rpm-ostree).
[ -w %{_localstatedir} ] && mkdir -p %{_localstatedir}/log/journal

[ -w %{_localstatedir} ] && journalctl --update-catalog || :
systemd-sysusers || :
systemd-tmpfiles --create &>/dev/null || :

# We reset the enablement of all services upon initial installation
# This will fix up enablement of any preset services that got installed
# before systemd due to rpm ordering problems:
# We also do this for user units.
systemctl preset-all &>/dev/null || :
systemctl --global preset-all &>/dev/null || :

%posttrans
if [ $1 -ge 2 ]; then
  [ -w %{_localstatedir} ] && journalctl --update-catalog || :

  systemctl daemon-reexec || :

  systemd-tmpfiles --create &>/dev/null || :
fi

%systemd_posttrans_with_restart systemd-timedated.service systemd-hostnamed.service systemd-journald.service systemd-localed.service systemd-userdbd.service

# FIXME: systemd-logind.service is excluded (https://github.com/systemd/systemd/pull/17558)

# This is the expanded form of %%systemd_user_daemon_reexec. We
# can't use the macro because we define it ourselves.
if [ $1 -ge 2 ] && [ -x "/usr/lib/systemd/systemd-update-helper" ]; then
    # Package upgrade, not uninstall
    /usr/lib/systemd/systemd-update-helper user-reexec || :
fi

%global udev_services %{shrink:
                        cryptsetup-pre.target
                        cryptsetup.target
                        hibernate.target
                        hybrid-sleep.target
                        initrd-cleanup.service
                        initrd-fs.target
                        initrd-parse-etc.service
                        initrd-root-device.target
                        initrd-root-fs.target
                        initrd-switch-root.service
                        initrd-switch-root.target
                        initrd-udevadm-cleanup-db.service
                        initrd-usr-fs.target
                        initrd.target
                        integritysetup-pre.target
                        integritysetup.target
                        kmod-static-nodes.service
                        proc-sys-fs-binfmt_misc.automount
                        proc-sys-fs-binfmt_misc.mount
                        quotaon-root.service
                        quotaon@.service
                        remote-cryptsetup.target
                        remote-veritysetup.target
                        sleep.target
                        suspend-then-hibernate.target
                        suspend.target
                        system-systemd\x2dcryptsetup.slice
                        system-systemd\x2dveritysetup.slice
                        systemd-backlight@.service
                        systemd-binfmt.service
                        systemd-bless-boot.service
                        systemd-bsod.service
                        systemd-coredump.socket
                        systemd-coredump@.service
                        systemd-fsck-root.service
                        systemd-fsck@.service
                        systemd-growfs-root.service
                        systemd-growfs@.service
                        systemd-hibernate-clear.service
                        systemd-hibernate-resume.service
                        systemd-hibernate.service
                        systemd-homed-activate.service
                        systemd-homed-firstboot.service
                        systemd-homed.service
                        systemd-hwdb-update.service
                        systemd-hybrid-sleep.service
                        systemd-modules-load.service
                        systemd-network-generator.service
                        systemd-oomd.service
                        systemd-oomd.socket
                        systemd-pcrextend.socket
                        systemd-pcrextend@.service
                        systemd-pcrfs-root.service
                        systemd-pcrfs@.service
                        systemd-pcrlock-file-system.service
                        systemd-pcrlock-firmware-code.service
                        systemd-pcrlock-firmware-config.service
                        systemd-pcrlock-machine-id.service
                        systemd-pcrlock-make-policy.service
                        systemd-pcrlock-secureboot-authority.service
                        systemd-pcrlock-secureboot-policy.service
                        systemd-pcrlock.socket
                        systemd-pcrlock@.service
                        systemd-pcrmachine.service
                        systemd-pcrphase-initrd.service
                        systemd-pcrphase-sysinit.service
                        systemd-pcrphase.service
                        systemd-portabled.service
                        systemd-pstore.service
                        systemd-quotacheck-root.service
                        systemd-quotacheck@.service
                        systemd-random-seed.service
                        systemd-remount-fs.service
                        systemd-rfkill.service
                        systemd-rfkill.socket
                        systemd-suspend-then-hibernate.service
                        systemd-suspend.service
                        systemd-sysctl.service
                        systemd-timesyncd.service
                        systemd-tmpfiles-setup-dev-early.service
                        systemd-tmpfiles-setup-dev.service
                        systemd-udev-load-credentials.service
                        systemd-udev-settle.service
                        systemd-udev-trigger.service
                        systemd-udevd-control.socket
                        systemd-udevd-kernel.socket
                        systemd-udevd.service
                        systemd-vconsole-setup.service
                        systemd-volatile-root.service
                        veritysetup-pre.target
                        veritysetup.target
                       }

%post udev
# Move old stuff around in /var/lib
mv %{_localstatedir}/lib/random-seed %{_localstatedir}/lib/systemd/random-seed &>/dev/null
mv %{_localstatedir}/lib/backlight %{_localstatedir}/lib/systemd/backlight &>/dev/null
if [ -L %{_localstatedir}/lib/systemd/timesync ]; then
    rm %{_localstatedir}/lib/systemd/timesync
    mv %{_localstatedir}/lib/private/systemd/timesync %{_localstatedir}/lib/systemd/timesync
fi
if [ -f %{_localstatedir}/lib/systemd/clock ]; then
    mkdir -p %{_localstatedir}/lib/systemd/timesync
    mv %{_localstatedir}/lib/systemd/clock %{_localstatedir}/lib/systemd/timesync/.
fi

systemd-hwdb update &>/dev/null

%systemd_post %udev_services
# Try to save the random seed, but don't complain if /dev/urandom is unavailable
/usr/lib/systemd/systemd-random-seed save 2>&1 | \
    grep -v 'Failed to open /dev/urandom' || :

# Replace obsolete keymaps
grep -q -E '^KEYMAP="?fi-latin[19]"?' /etc/vconsole.conf 2>/dev/null &&
    sed -i.rpm.bak -r 's/^KEYMAP="?fi-latin[19]"?/KEYMAP="fi"/' /etc/vconsole.conf || :

%preun udev
%systemd_preun %udev_services
%posttrans udev
# Restart some services.
# Others are either oneshot services, or sockets, and restarting them causes issues (#1378974)
%systemd_posttrans_with_restart systemd-udevd.service systemd-timesyncd.service systemd-homed.service systemd-oomd.service systemd-portabled.service

%if %{with journal_remote}
%global journal_remote_units_restart systemd-journal-gatewayd.service systemd-journal-remote.service systemd-journal-upload.service
%global journal_remote_units_norestart systemd-journal-gatewayd.socket systemd-journal-remote.socket
%post journal-remote
%systemd_post %journal_remote_units_restart %journal_remote_units_norestart
%firewalld_reload
%preun journal-remote
%systemd_preun %journal_remote_units_restart %journal_remote_units_norestart
if [ $1 -eq 1 ] ; then
    if [ -f %{_localstatedir}/lib/systemd/journal-upload/state -a ! -L %{_localstatedir}/lib/systemd/journal-upload ] ; then
        mkdir -p %{_localstatedir}/lib/private/systemd/journal-upload
        mv %{_localstatedir}/lib/systemd/journal-upload/state %{_localstatedir}/lib/private/systemd/journal-upload/.
        rmdir %{_localstatedir}/lib/systemd/journal-upload || :
    fi
fi

%posttrans journal-remote
%systemd_posttrans_with_restart %journal_remote_units_restart
%firewalld_reload
%endif

%if %{with network}
%global networkd_services %{shrink:
                            systemd-networkd.service
                            systemd-networkd.socket
                            systemd-networkd-wait-online.service
                            systemd-network-generator.service
                            systemd-networkd-persistent-storage.service
                           }

%post networkd
# systemd-networkd was split out in systemd-246.6-2.
# Ideally, we would have a trigger scriptlet to record enablement
# state when upgrading from systemd <= systemd-246.6-1. But, AFAICS,
# rpm doesn't allow us to trigger on another package, short of
# querying the rpm database ourselves, which seems risky. For rpm,
# systemd and systemd-networkd are completely unrelated.  So let's use
# a hack to detect if an old systemd version is currently present in
# the file system.
if [ $1 -eq 1 ] && ls /usr/lib/systemd/libsystemd-shared-24[0-6].so &>/dev/null; then
    echo "Skipping presets for systemd-networkd.service, seems we are upgrading from old systemd."
else
    %systemd_post %networkd_services
fi

%preun networkd
%systemd_preun %networkd_services
%posttrans networkd
%systemd_posttrans_with_restart systemd-networkd.service

%post resolved
[ $1 -eq 1 ] || exit 0
# Initial installation

touch %{_localstatedir}/lib/rpm-state/systemd-resolved.initial-installation

if ls /usr/lib/systemd/libsystemd-shared-24[0-8].so &>/dev/null; then
    echo "Skipping presets for systemd-resolved.service, seems we are upgrading from old systemd."
    exit 0
fi

%systemd_post systemd-resolved.service

%preun resolved
%systemd_preun systemd-resolved.service
if [ $1 -eq 0 ] ; then
        if [ -L /etc/resolv.conf ] && \
            realpath /etc/resolv.conf | grep ^/run/systemd/resolve/; then
                rm -f /etc/resolv.conf # no longer useful
                # if network manager is enabled, move to it instead
                [ -f /run/NetworkManager/resolv.conf ] && \
                systemctl -q is-enabled NetworkManager.service &>/dev/null && \
                    ln -fsv ../run/NetworkManager/resolv.conf /etc/resolv.conf
        fi
fi

%posttrans resolved
%systemd_posttrans_with_restart systemd-resolved.service
[ -e %{_localstatedir}/lib/rpm-state/systemd-resolved.initial-installation ] || exit 0
rm %{_localstatedir}/lib/rpm-state/systemd-resolved.initial-installation
# Initial installation

# Create /etc/resolv.conf symlink.
#
# We would also create it using tmpfiles, but let's do this here too
# before NetworkManager gets a chance. (systemd-tmpfiles invocation
# above does not do this, because the line is marked with ! and
# tmpfiles is invoked without --boot in the scriptlet.)
#
# *Create* the symlink if nothing is present yet.
#
# *Override* the symlink if systemd is running. Don't do it if systemd
# is not running, because that will immediately break DNS resolution,
# since systemd-resolved is also not running
#
# Also don't create the symlink to the stub when the stub is disabled (#1891847 again).
if systemctl -q is-enabled systemd-resolved.service &>/dev/null &&
   ! systemd-analyze cat-config systemd/resolved.conf 2>/dev/null |
        grep -iqE '^DNSStubListener\s*=\s*(no?|false|0|off)\s*$'; then

  if ! test -e /etc/resolv.conf && ! test -L /etc/resolv.conf; then
    ln -sv ../run/systemd/resolve/stub-resolv.conf /etc/resolv.conf || :
  elif test -d /run/systemd/system/ &&
     ! mountpoint /etc/resolv.conf &>/dev/null; then
    ln -fsv ../run/systemd/resolve/stub-resolv.conf /etc/resolv.conf || :
  fi
fi
%endif

%files
%license LICENSE.GPL2 LICENSES/*.txt
%doc README README.md NEWS
%exclude %{_docdir}/systemd/LICENSE*
%doc %{_prefix}/lib/modprobe.d/README
%doc %{_prefix}/lib/sysctl.d/README
%doc %{_prefix}/lib/tmpfiles.d/README
%doc %{_docdir}/systemd/CODING_STYLE.md
%doc %{_docdir}/systemd/DISTRO_PORTING.md
%doc %{_docdir}/systemd/ENVIRONMENT.md
%doc %{_docdir}/systemd/HACKING.md
%doc %{_docdir}/systemd/NEWS
%doc %{_docdir}/systemd/README
%doc %{_docdir}/systemd/README.logs
%doc %{_docdir}/systemd/TRANSIENT-SETTINGS.md
%doc %{_docdir}/systemd/TRANSLATORS.md
%doc %{_docdir}/systemd/UIDS-GIDS.md
%ghost %dir %attr(0755,-,-) /etc/systemd/system/basic.target.wants
%ghost %dir %attr(0755,-,-) /etc/systemd/system/default.target.wants
%ghost %dir %attr(0755,-,-) /etc/systemd/system/multi-user.target.wants
%ghost %dir %attr(0755,-,-) /etc/systemd/system/sockets.target.wants
%ghost %dir %attr(0755,-,-) /etc/systemd/system/sysinit.target.wants
%{_sysconfdir}/systemd/journald.conf
%{_sysconfdir}/systemd/logind.conf
%{_sysconfdir}/systemd/system.conf
%{_sysconfdir}/systemd/user.conf
%{_prefix}/lib/tmpfiles.d/20-*
%{_prefix}/lib/tmpfiles.d/credstore.conf
%{_prefix}/lib/tmpfiles.d/etc.conf
%{_prefix}/lib/tmpfiles.d/home.conf
%{_prefix}/lib/tmpfiles.d/journal-nocow.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/portables.conf
%{_prefix}/lib/tmpfiles.d/provision.conf
%{_prefix}/lib/tmpfiles.d/static-nodes-permissions.conf
%{_prefix}/lib/tmpfiles.d/systemd-nologin.conf
%{_prefix}/lib/tmpfiles.d/systemd-tmp.conf
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%{_prefix}/lib/tmpfiles.d/var.conf
%{_prefix}/lib/tmpfiles.d/x11.conf
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/busctl
%{_datadir}/bash-completion/completions/coredumpctl
%{_datadir}/bash-completion/completions/hostnamectl
%{_datadir}/bash-completion/completions/journalctl
%{_datadir}/bash-completion/completions/localectl
%{_datadir}/bash-completion/completions/loginctl
%{_datadir}/bash-completion/completions/oomctl
%{_datadir}/bash-completion/completions/portablectl
%{_datadir}/bash-completion/completions/run0
%{_datadir}/bash-completion/completions/systemctl
%{_datadir}/bash-completion/completions/systemd-analyze
%{_datadir}/bash-completion/completions/systemd-cat
%{_datadir}/bash-completion/completions/systemd-cgls
%{_datadir}/bash-completion/completions/systemd-cgtop
%{_datadir}/bash-completion/completions/systemd-confext
%{_datadir}/bash-completion/completions/systemd-creds
%{_datadir}/bash-completion/completions/systemd-delta
%{_datadir}/bash-completion/completions/systemd-detect-virt
%{_datadir}/bash-completion/completions/systemd-id128
%{_datadir}/bash-completion/completions/systemd-path
%{_datadir}/bash-completion/completions/systemd-run
%{_datadir}/bash-completion/completions/systemd-sysext
%{_datadir}/factory/etc/issue
%{_datadir}/factory/etc/locale.conf
%{_datadir}/factory/etc/nsswitch.conf
%{_datadir}/factory/etc/pam.d/*
%{_datadir}/mime/packages/io.systemd.xml
%{_bindir}/busctl
%{_bindir}/coredumpctl
%{_bindir}/hostnamectl
%{_bindir}/journalctl
%{_bindir}/localectl
%{_bindir}/loginctl
%{_bindir}/oomctl
%{_bindir}/run0
%{_bindir}/systemctl
%{_bindir}/systemd-ac-power
%{_bindir}/systemd-analyze
%{_bindir}/systemd-ask-password
%{_bindir}/systemd-cat
%{_bindir}/systemd-cgls
%{_bindir}/systemd-cgtop
%{_bindir}/systemd-confext
%{_bindir}/systemd-creds
%{_bindir}/systemd-delta
%{_bindir}/systemd-detect-virt
%{_bindir}/systemd-escape
%{_bindir}/systemd-firstboot
%{_bindir}/systemd-id128
%{_bindir}/systemd-inhibit
%{_bindir}/systemd-machine-id-setup
%{_bindir}/systemd-mount
%{_bindir}/systemd-notify
%{_bindir}/systemd-path
%{_bindir}/systemd-run
%{_bindir}/systemd-socket-activate
%{_bindir}/systemd-stdio-bridge
%{_bindir}/systemd-sysext
%{_bindir}/systemd-tmpfiles
%{_bindir}/systemd-tty-ask-password-agent
%{_bindir}/systemd-umount
%{_bindir}/systemd-vpick
%{_bindir}/timedatectl
%{_bindir}/userdbctl
%{_bindir}/varlinkctl
%{_bindir}/halt
%{_bindir}/init
%{_bindir}/poweroff
%{_bindir}/reboot
%{_bindir}/shutdown
%{_bindir}/runlevel
%{_bindir}/telinit
%if %{with bpf}
%{_bindir}/systemd-bpf
%endif
%{_prefix}/lib/pam.d/systemd-*
%dir %{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/system-services/org.freedesktop.hostname1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.locale1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.login1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.timedate1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.oom1.service
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.locale1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.login1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.oom1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.freedesktop.hostname1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.locale1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.login1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.systemd1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.timedate1.policy
%{_datadir}/polkit-1/actions/io.systemd.credentials.policy
%{_datadir}/polkit-1/actions/io.systemd.mount-file-system.policy
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%dir %{_datadir}/systemd
%{_datadir}/systemd/kbd-model-map
%{_datadir}/systemd/language-fallback-map
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_busctl
%{_datadir}/zsh/site-functions/_coredumpctl
%{_datadir}/zsh/site-functions/_hostnamectl
%{_datadir}/zsh/site-functions/_journalctl
%{_datadir}/zsh/site-functions/_localectl
%{_datadir}/zsh/site-functions/_loginctl
%{_datadir}/zsh/site-functions/_run0
%{_datadir}/zsh/site-functions/_sd_hosts_or_user_at_host
%{_datadir}/zsh/site-functions/_sd_outputmodes
%{_datadir}/zsh/site-functions/_sd_unit_files
%{_datadir}/zsh/site-functions/_systemctl
%{_datadir}/zsh/site-functions/_systemd
%{_datadir}/zsh/site-functions/_systemd-analyze
%{_datadir}/zsh/site-functions/_systemd-delta
%{_datadir}/zsh/site-functions/_systemd-inhibit
%{_datadir}/zsh/site-functions/_systemd-path
%{_datadir}/zsh/site-functions/_systemd-run
%{_datadir}/zsh/site-functions/_systemd-tmpfiles
%{_datadir}/zsh/site-functions/_timedatectl
%{_datadir}/zsh/site-functions/_oomctl
%{_datadir}/zsh/site-functions/_sd_machines
%{_datadir}/zsh/site-functions/_varlinkctl
%if %{with bpf}
%{_datadir}/zsh/site-functions/_systemd-bpf
%endif
%exclude %{_sysconfdir}/sysctl.conf
%{_sysconfdir}/sysctl.d/99-sysctl.conf
%{pkgdir}/
%{_rundir}/utmp
%{_prefix}/lib/environment.d/99-environment.conf
%{_sysconfdir}/ssh/ssh_config.d/20-systemd-ssh-proxy.conf
%{_sysconfdir}/profile.d/70-systemd-shell-extra.sh
%{_sysconfdir}/X11/xinit/xinitrc.d/50-systemd-user.sh
%{_localstatedir}/lib/systemd/catalog/database
%{_localstatedir}/log/btmp
%{_localstatedir}/log/lastlog
%{_localstatedir}/log/wtmp
%{_sysconfdir}/xdg/systemd/user
%ghost /etc/hostname
%ghost /etc/locale.conf
%ghost /etc/localtime
%ghost /etc/machine-id
%ghost /etc/machine-info
%ghost /etc/vconsole.conf
%ghost /etc/X11/xorg.conf.d/00-keyboard.conf
%ghost /etc/crypttab
# We still got some files installed even if certain features are disabled
%if %{without network}
%exclude %{_sysconfdir}/systemd/networkd.conf
%exclude %{_sysconfdir}/systemd/resolved.conf
%endif
%if %{without journal_remote}
%exclude %{_sysconfdir}/systemd/journal-remote.conf
%exclude %{_sysconfdir}/systemd/journal-upload.conf
%exclude %{_localstatedir}/lib/systemd/journal-upload
%endif
%exclude %{_datadir}/bash-completion/completions/bootctl
%exclude %{_datadir}/zsh/site-functions/_bootctl

%files -n kernel-install
%{_bindir}/kernel-install
%{_prefix}/lib/kernel/install.conf
%{_prefix}/lib/kernel/install.d/50-depmod.install
%{_prefix}/lib/kernel/install.d/90-loaderentry.install
%{_prefix}/lib/kernel/install.d/90-uki-copy.install
%{_datadir}/zsh/site-functions/_kernel-install
%{_datadir}/bash-completion/completions/kernel-install

%files libs
%license LICENSE.LGPL2.1
%{_libdir}/lib*.so.*

%files shared
%license LICENSE.LGPL2.1
%license LICENSES/MIT.txt
%{_libdir}/systemd/*

%files pam
%{_libdir}/security/*.so

%files rpm-macros
%{_rpmmacrodir}/macros.systemd

%files repart
%{_bindir}/systemd-repart

%files dissect
%{_bindir}/mount.ddi
%{_bindir}/systemd-dissect
%{_datadir}/bash-completion/completions/systemd-dissect

%files sysusers
%{_bindir}/systemd-sysusers
%if %{with docs}
%{_mandir}/man1/systemd-sysusers.1.gz
%{_mandir}/man5/sysusers.d.5.gz
%{_mandir}/man8/systemd-sysusers.service.8.gz
%endif
%{_prefix}/lib/sysusers.d
%{_prefix}/lib/systemd/system/systemd-sysusers.service

%if %{with network}
%files resolved
%{_bindir}/systemd-resolve
%{_bindir}/resolvectl
%{_bindir}/resolvconf
%{_sysconfdir}/systemd/resolved.conf
%{_prefix}/lib/tmpfiles.d/systemd-resolve.conf
%{_datadir}/bash-completion/completions/resolvectl
%{_datadir}/bash-completion/completions/systemd-resolve
%if %{with docs}
%{_mandir}/man1/resolvectl.1.gz
%{_mandir}/man5/resolved.conf.5.gz
%{_mandir}/man5/resolved.conf.d.5.gz
%{_mandir}/man8/libnss_resolve.so.2.8.gz
%{_mandir}/man8/nss-resolve.8.gz
%{_mandir}/man8/systemd-resolved.8.gz
%{_mandir}/man8/systemd-resolved.service.8.gz
%endif
%dir %{_datadir}/dbus-1/interfaces
%{_datadir}/dbus-1/interfaces/org.freedesktop.resolve1.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.resolve1.Link.xml
%dir %{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/system-services/org.freedesktop.resolve1.service
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.freedesktop.resolve1.conf
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.freedesktop.resolve1.policy
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/resolvectl
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_resolvectl
%{_libdir}/libnss_resolve.so.2
%{_prefix}/lib/systemd/system/systemd-resolved.service
%ghost /etc/resolv.conf
%endif

%files devel
%{_includedir}/systemd/
%{_includedir}/libudev.h
%{_libdir}/libsystemd.so
%{_libdir}/libudev.so
%{_libdir}/pkgconfig/libsystemd.pc
%{_libdir}/pkgconfig/libudev.pc
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/pkgconfig/systemd.pc
%{_datadir}/pkgconfig/udev.pc
%{_datadir}/bash-completion/completions/systemd-vpick
%{_datadir}/bash-completion/completions/timedatectl
%if %{with bpf}
%{_datadir}/bash-completion/completions/systemd-bpf
%endif

%files udev
%{_bindir}/systemd-hwdb
%{_bindir}/udevadm
%{_sysconfdir}/systemd/coredump.conf
%{_sysconfdir}/systemd/homed.conf
%{_sysconfdir}/systemd/oomd.conf
%{_sysconfdir}/systemd/pstore.conf
%{_sysconfdir}/systemd/sleep.conf
%{_sysconfdir}/systemd/timesyncd.conf
%{_prefix}/lib/sysctl.d/50-*
%{_prefix}/lib/tmpfiles.d/systemd-pstore.conf
%{_datadir}/bash-completion/completions/bootctl
%{_localstatedir}/lib/systemd/random-seed
%{_localstatedir}/lib/systemd/timesync/clock
%if %{with docs}
%{_mandir}/man8/udevadm.8.gz
%{_mandir}/man7/udev.7.gz
%{_mandir}/man5/udev.conf.5.gz
%{_mandir}/man5/hwdb.7.gz
%{_mandir}/man5/systemd.dnssd.5.gz
%{_mandir}/man5/systemd.link.5.gz
%{_mandir}/man5/systemd.netdev.5.gz
%{_mandir}/man5/systemd.network.5.gz
%{_mandir}/man8/systemd-hwdb.8.gz
%endif
%{_sysconfdir}/udev
%{_prefix}/lib/udev/ata_id
%{_prefix}/lib/udev/cdrom_id
%{_prefix}/lib/udev/dmi_memory_id
%if %{with fido2}
%{_prefix}/lib/udev/fido_id
%else
%exclude %{_prefix}/lib/udev/fido_id
%endif
%{_prefix}/lib/udev/iocost
%{_prefix}/lib/udev/iocost.conf
%{_prefix}/lib/udev/mtd_probe
%{_prefix}/lib/udev/scsi_id
%{_prefix}/lib/udev/udev.conf
%{_prefix}/lib/udev/v4l_id
%{_prefix}/lib/udev/hwdb.d/*
%{_prefix}/lib/udev/rules.d/*
%{_datadir}/bash-completion/completions/udevadm
%{_datadir}/zsh/site-functions/_udevadm
%{_prefix}/lib/modprobe.d/systemd.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.timesync1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.timesync1.conf
%{_datadir}/polkit-1/actions/org.freedesktop.timesync1.policy
%{_datadir}/factory/etc/vconsole.conf

%if %{with ukify}
%files ukify
%{_bindir}/ukify
%{_prefix}/lib/kernel/install.d/60-ukify.install
%{_prefix}/lib/kernel/uki.conf
%{_prefix}/lib/systemd/ukify
%if %{with docs}
%{_mandir}/man1/ukify.1.gz
%endif
%endif

%files boot
%{_prefix}/lib/systemd/boot/efi/systemd-boot*.efi
# %%{_prefix}/lib/systemd/boot/efi/systemd-stub*.efi
%if %{with docs}
%{_mandir}/man8/bootctl.8.gz
%{_mandir}/man7/systemd-boot.7.gz
%{_mandir}/man5/loader.conf.5.gz
%endif
%{_bindir}/bootctl
%{_datadir}/bash-completion/completions/bootctl
%{_datadir}/zsh/site-functions/_bootctl

%files container
%ghost %dir %attr(0700,-,-) /var/lib/machines
%{_bindir}/machinectl
%{_bindir}/portablectl
%{_bindir}/systemd-nspawn
%{_prefix}/lib/tmpfiles.d/systemd-nspawn.conf
%{_datadir}/bash-completion/completions/systemd-nspawn
%if %{with docs}
%{_mandir}/man1/machinectl.1.gz
%{_mandir}/man1/portablectl.1.gz
%{_mandir}/man1/systemd-nspawn.1.gz
%{_mandir}/man5/nspawn.5.gz
%{_mandir}/man5/portabled.conf.5.gz
%{_mandir}/man5/portabled.conf.d.5.gz
%{_mandir}/man8/systemd-machined.service.8.gz
%{_mandir}/man8/systemd-portabled.service.8.gz
%endif
%dir %{_datadir}/dbus-1/interfaces
%{_datadir}/dbus-1/interfaces/org.freedesktop.machine1.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portable1.Manager.xml
%dir %{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/system-services/org.freedesktop.machine1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.portable1.service
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.freedesktop.machine1.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.portable1.conf
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.freedesktop.machine1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.portable1.policy
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/machinectl
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_machinectl
%{_datadir}/zsh/site-functions/_systemd-nspawn
%{_prefix}/lib/systemd/system/machines.target
%{_prefix}/lib/systemd/system/systemd-machined.service
%{_prefix}/lib/systemd/system/systemd-portabled.service
%{_prefix}/lib/systemd/system/systemd-nspawn@.service

%if %{with journal_remote}
%files journal-remote
%{_bindir}/systemd-journal-gatewayd
%{_bindir}/systemd-journal-remote
%{_bindir}/systemd-journal-upload
%{_sysconfdir}/systemd/journal-remote.conf
%{_sysconfdir}/systemd/journal-upload.conf
%if %{with docs}
%{_mandir}/man8/systemd-journal-gatewayd.8.gz
%{_mandir}/man8/systemd-journal-gatewayd.service.8.gz
%{_mandir}/man8/systemd-journal-gatewayd.socket.8.gz
%{_mandir}/man8/systemd-journal-remote.8.gz
%{_mandir}/man8/systemd-journal-remote.service.8.gz
%{_mandir}/man8/systemd-journal-remote.socket.8.gz
%{_mandir}/man8/systemd-journal-upload.8.gz
%{_mandir}/man8/systemd-journal-upload.service.8.gz
%{_mandir}/man5/journal-remote.conf.5.gz
%{_mandir}/man5/journal-remote.conf.d.5.gz
%{_mandir}/man5/journal-upload.conf.5.gz
%{_mandir}/man5/journal-upload.conf.d.5.gz
%endif
%{_prefix}/lib/systemd/system/systemd-journal-gatewayd.service
%{_prefix}/lib/systemd/system/systemd-journal-gatewayd.socket
%{_prefix}/lib/systemd/system/systemd-journal-remote.service
%{_prefix}/lib/systemd/system/systemd-journal-remote.socket
%{_prefix}/lib/systemd/system/systemd-journal-upload.service
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-journal-gatewayd.socket
%{_prefix}/lib/systemd/system/sockets.target.wants/systemd-journal-remote.socket
%dir %{_localstatedir}/lib/systemd/journal-upload
%ghost %{_localstatedir}/lib/systemd/journal-upload/state
%dir %{_localstatedir}/cache/systemd/journal-remote
%{_localstatedir}/lib/private/systemd/journal-upload/state
%endif

%if %{with network}
%files networkd
%{_bindir}/networkctl
%{_sysconfdir}/systemd/networkd.conf
%{_prefix}/lib/tmpfiles.d/systemd-network.conf
%{_datadir}/bash-completion/completions/networkctl
%if %{with docs}
%{_mandir}/man1/networkctl.1.gz
%{_mandir}/man5/networkd.conf.5.gz
%{_mandir}/man5/networkd.conf.d.5.gz
%{_mandir}/man8/systemd-networkd.8.gz
%{_mandir}/man8/systemd-networkd.service.8.gz
%{_mandir}/man8/systemd-networkd-wait-online.8.gz
%{_mandir}/man8/systemd-networkd-wait-online.service.8.gz
%endif
%dir %{_datadir}/dbus-1/interfaces
%{_datadir}/dbus-1/interfaces/org.freedesktop.network1.Manager.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.network1.Link.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.network1.Network.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.network1.DHCPServer.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.network1.DHCPv6Client.xml
%dir %{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/system-services/org.freedesktop.network1.service
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/org.freedesktop.network1.conf
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.freedesktop.network1.policy
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/networkctl
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_networkctl
%dir %{_prefix}/lib/systemd
%{_prefix}/lib/systemd/network
%{_prefix}/lib/systemd/system/systemd-networkd.service
%{_prefix}/lib/systemd/system/systemd-networkd.socket
%{_prefix}/lib/systemd/system/systemd-networkd-wait-online.service

%files networkd-defaults
%dir %{_prefix}/lib/systemd/network
%{_prefix}/lib/systemd/network/99-default.link
%endif

%files oomd-defaults

%changelog
%{?autochangelog}
