# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iptables
Version:        1.8.11
Release:        %autorelease
Summary:        Tools for managing Linux kernel packet filtering capabilities
License:        GPL-2.0-only AND Artistic-2.0 AND ISC
URL:            https://www.netfilter.org/projects/iptables
VCS:            git:https://git.netfilter.org/iptables
#!RemoteAsset
Source0:        %{url}/files/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        %{url}/files/%{name}-%{version}.tar.xz.sig
Source2:        iptables.service
Source3:        arptables.service
Source4:        ebtables.service
Source5:        empty.rules
BuildSystem:    autotools

BuildOption(conf):  --enable-devel
BuildOption(conf):  --enable-bpf-compiler
BuildOption(conf):  --with-kernel=%{_prefix}
BuildOption(conf):  --with-kbuild=%{_prefix}
BuildOption(conf):  --with-ksource=%{_prefix}

BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnetfilter_conntrack)
BuildRequires:  pkgconfig(libnfnetlink)
BuildRequires:  pkgconfig(libnftnl)
BuildRequires:  pkgconfig(libpcap)

# for tests
BuildRequires:  python3

%description
The iptables utility controls the network packet filtering code in the
Linux kernel. If you need to set up firewalls and/or IP masquerading,
you should install this package.

%package        libs
Summary:        libxtables and iptables extensions userspace support

%description    libs
libxtables and associated shared object files

Libxtables provides unified access to iptables extensions in userspace. Data
and logic for those is kept in per-extension shared object files.

%package        devel
Summary:        Development package for iptables
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
libxtables development headers and pkgconfig files

%package        utils
Summary:        iptables and ip6tables misc utilities
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
Utils for iptables

This package provides nfnl_osf with the pf.os database and nfbpf_compile,
a bytecode generator for use with xt_bpf. Also included is iptables-apply,
a safer way to update iptables remotely.

%package        nft
Summary:        nftables compatibility for iptables, arptables and ebtables
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires(post): update-alternatives
Requires(post): /usr/bin/readlink
Requires(postun): update-alternatives
Provides:       arptables-helper
Provides:       iptables
Provides:       arptables
Provides:       ebtables

%description    nft
nftables compatibility for iptables, arptables and ebtables.

%package        services
Summary:        iptables and ip6tables services for iptables
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-utils%{?_isa} = %{version}-%{release}
%{?systemd_ordering}
Provides:       arptables-services = %{version}-%{release}
Provides:       ebtables-services = %{version}-%{release}
BuildArch:      noarch

%description    services
iptables services for IPv4 and IPv6

This package provides the services iptables and ip6tables that have been split
out of the base package since they are not active by default anymore.

%package        legacy
Summary:        Legacy tools for managing Linux kernel packet filtering capabilities
Requires:       %{name}-legacy-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       %{name}-compat = %{version}-%{release}

%description    legacy
The iptables utility controls the network packet filtering code in the
Linux kernel. This package contains the legacy tools which are obsoleted by
nft-variants in iptables-nft package for backwards compatibility reasons.
If you need to set up firewalls and/or IP masquerading, you should not install
this package but either nftables or iptables-nft instead.

%package        legacy-libs
Summary:        iptables legacy libraries

%description    legacy-libs
iptables libraries.

Please remember that libip*tc libraries do neither have a stable API nor a real
so version. For more information about this, please have a look at

  http://www.netfilter.org/documentation/FAQ/netfilter-faq-4.html#ss4.5

%package        legacy-devel
Summary:        Development package for legacy iptables
Requires:       %{name}-legacy-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    legacy-devel
Legacy iptables development headers and pkgconfig files

%conf -p
./autogen.sh
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"

%build -p
# do not use rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

rm -f include/linux/types.h

%install -a
# install systemd service files
install -d -m 755 %{buildroot}/%{_unitdir}
install -c -m 644 %{SOURCE2} %{SOURCE3} %{SOURCE4} %{buildroot}/%{_unitdir}
sed -e 's;iptables;ip6tables;g' -e 's;IPv4;IPv6;g' -e 's;/usr/libexec/ip6tables;/usr/libexec/iptables;g' < %{SOURCE5} > ip6tables.service
install -c -m 644 ip6tables.service %{buildroot}/%{_unitdir}

# install configuration files
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -c -m 600 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/iptables
install -c -m 600 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/ip6tables
echo '# Configure prior to use' > %{buildroot}%{_sysconfdir}/sysconfig/arptables
touch %{buildroot}%{_sysconfdir}/sysconfig/ebtables

# Remove /etc/ethertypes (part of setup)
rm -f %{buildroot}%{_sysconfdir}/ethertypes

# prepare for alternatives
touch %{buildroot}%{_mandir}/man8/arptables.8
touch %{buildroot}%{_mandir}/man8/arptables-save.8
touch %{buildroot}%{_mandir}/man8/arptables-restore.8
touch %{buildroot}%{_mandir}/man8/ebtables.8
rm %{buildroot}%{_sbindir}/{ip,ip6,arp,eb}tables{,-save,-restore}
touch %{buildroot}%{_sbindir}/{ip,ip6,arp,eb}tables{,-save,-restore}

# fix absolute symlink
ln -sf --relative %{buildroot}%{_sbindir}/xtables-legacy-multi %{buildroot}%{_bindir}/iptables-xml

# install legacy actions for service command
install -d %{buildroot}/%{legacy_actions}/iptables
install -d %{buildroot}/%{legacy_actions}/ip6tables

# test require root
%check

%post services
%systemd_post arptables.service ebtables.service
%systemd_post iptables.service ip6tables.service

%preun services
%systemd_preun arptables.service ebtables.service
%systemd_preun iptables.service ip6tables.service

%postun services
%systemd_postun arptables.service ebtables.service
%systemd_postun iptables.service ip6tables.service

%post -e nft
[[ %%{_excludedocs} == 1 ]] || do_man=true

# remove non-symlinks in spots managed by alternatives
# to cover for updates from not-yet-alternatived versions
for pfx in %{_prefix}/sbin/{eb,arp}tables; do
    for sfx in "" "-restore" "-save"; do
        if [ "$(readlink -e $pfx$sfx)" == $pfx$sfx ]; then
            rm -f $pfx$sfx
        fi
    done
done
for manpfx in %{_mandir}/man8/{eb,arp}tables; do
    for sfx in {,-restore,-save}.8.gz; do
        if [ "$(readlink -e $manpfx$sfx)" == $manpfx$sfx ]; then
            rm -f $manpfx$sfx
        fi
    done
done

pfx=%{_sbindir}/iptables
pfx6=%{_sbindir}/ip6tables
update-alternatives --install \
    $pfx iptables $pfx-nft 10 \
    --follower $pfx6 ip6tables $pfx6-nft \
    --follower $pfx-restore iptables-restore $pfx-nft-restore \
    --follower $pfx-save iptables-save $pfx-nft-save \
    --follower $pfx6-restore ip6tables-restore $pfx6-nft-restore \
    --follower $pfx6-save ip6tables-save $pfx6-nft-save

pfx=%{_sbindir}/ebtables
manpfx=%{_mandir}/man8/ebtables
update-alternatives --install \
    $pfx ebtables $pfx-nft 10 \
    --follower $pfx-save ebtables-save $pfx-nft-save \
    --follower $pfx-restore ebtables-restore $pfx-nft-restore \
    ${do_man:+--follower $manpfx.8.gz ebtables-man $manpfx-nft.8.gz}

pfx=%{_sbindir}/arptables
manpfx=%{_mandir}/man8/arptables
update-alternatives --install \
    $pfx arptables $pfx-nft 10 \
    --follower $pfx-save arptables-save $pfx-nft-save \
    --follower $pfx-restore arptables-restore $pfx-nft-restore \
    ${do_man:+--follower $manpfx.8.gz arptables-man $manpfx-nft.8.gz} \
    ${do_man:+--follower $manpfx-save.8.gz arptables-save-man $manpfx-nft-save.8.gz} \
    ${do_man:+--follower $manpfx-restore.8.gz arptables-restore-man $manpfx-nft-restore.8.gz}

# TODO: In the future we might merge %%%{_sbindir} and %%{_bindir}? - 251
for name in ip{,6}tables{,-save,-restore} ebtables{,-save,-restore} arptables{,-save,-restore}; do
    test -h /usr/sbin || ln -s ../bin/$name /usr/sbin/$name 2>/dev/null || :
done

%postun nft
if [ $1 -eq 0 ]; then
    for cmd in iptables ebtables arptables; do
        update-alternatives --remove $cmd %{_sbindir}/$cmd-nft
    done
fi

%post legacy
pfx=%{_sbindir}/iptables
pfx6=%{_sbindir}/ip6tables
update-alternatives --install \
    $pfx iptables $pfx-legacy 10 \
    --follower $pfx6 ip6tables $pfx6-legacy \
    --follower $pfx-restore iptables-restore $pfx-legacy-restore \
    --follower $pfx-save iptables-save $pfx-legacy-save \
    --follower $pfx6-restore ip6tables-restore $pfx6-legacy-restore \
    --follower $pfx6-save ip6tables-save $pfx6-legacy-save

# TODO: In the future we might merge %%%{_sbindir} and %%{_bindir}? - 251
for name in ip{,6}tables{,-save,-restore}; do
   test -h /usr/sbin || ln -s ../bin/$name /usr/sbin/$name 2>/dev/null || :
done

%postun legacy
if [ $1 -eq 0 ]; then
    update-alternatives --remove \
        iptables %{_sbindir}/iptables-legacy
fi

%files libs
%{_libdir}/libxtables.so.12*
%dir %{_libdir}/xtables
%{_libdir}/xtables/lib{ip,ip6,x}t*
%{_mandir}/man8/ip{,6}tables.8.gz
%{_mandir}/man8/ip{,6}tables-{extensions,save,restore}.8.gz

%files devel
%{_includedir}/xtables{,-version}.h
%{_libdir}/libxtables.so
%{_libdir}/pkgconfig/xtables.pc

%files utils
%{_sbindir}/nfnl_osf
%{_sbindir}/nfbpf_compile
%{_sbindir}/ip{,6}tables-apply
%dir %{_datadir}/xtables
%{_datadir}/xtables/pf.os
%{_mandir}/man8/nfnl_osf*
%{_mandir}/man8/nfbpf_compile*
%{_mandir}/man8/ip{,6}tables-apply*

%files nft
%{_sbindir}/ip{,6}tables-nft*
%{_sbindir}/ip{,6}tables{,-restore}-translate
%{_sbindir}/{eb,arp}tables-nft*
%{_sbindir}/xtables-nft-multi
%{_sbindir}/xtables-monitor
%{_sbindir}/ebtables-translate
%{_sbindir}/arptables-translate
%dir %{_libdir}/xtables
%{_libdir}/xtables/lib{arp,eb}t*
%{_mandir}/man8/xtables-monitor*
%{_mandir}/man8/xtables-translate*
%{_mandir}/man8/*-nft*
%{_mandir}/man8/ip{,6}tables{,-restore}-translate*
%{_mandir}/man8/ebtables-translate*
%{_mandir}/man8/arptables-translate*
%ghost %attr(0755,root,root) %{_sbindir}/ip{,6}tables{,-save,-restore}
%ghost %attr(0755,root,root) %{_sbindir}/{eb,arp}tables{,-save,-restore}
%ghost %{_mandir}/man8/arptables{,-save,-restore}.8.gz
%ghost %{_mandir}/man8/ebtables.8.gz

%files services
%config(noreplace) %{_sysconfdir}/sysconfig/ip{,6}tables
%config(noreplace) %{_sysconfdir}/sysconfig/arptables
%ghost %{_sysconfdir}/sysconfig/ebtables
%{_unitdir}/{arp,eb,ip,ip6}tables.service

%files legacy
%{_sbindir}/ip{,6}tables-legacy*
%{_sbindir}/xtables-legacy-multi
%{_bindir}/iptables-xml
%{_mandir}/man1/iptables-xml*
%{_mandir}/man8/xtables-legacy*
%dir %{_datadir}/xtables
%{_datadir}/xtables/iptables.xslt
%ghost %attr(0755,root,root) %{_sbindir}/ip{,6}tables{,-save,-restore}

%files legacy-libs
%license COPYING
%{_libdir}/libip{4,6}tc.so.*

%files legacy-devel
%dir %{_includedir}/libiptc
%{_includedir}/libiptc/*.h
%{_libdir}/libip*tc.so
%{_libdir}/pkgconfig/libip{,4,6}tc.pc

%changelog
%autochangelog
