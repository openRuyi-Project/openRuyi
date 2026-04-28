# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global idmap_modules  idmap_ad,idmap_rid,idmap_ldap,idmap_hash,idmap_tdb2
%global pdb_modules    pdb_tdbsam,pdb_ldap,pdb_smbpasswd,pdb_wbc_sam,pdb_samba4
%global auth_modules   auth_wbc,auth_unix,auth_server,auth_samba4,auth_skel
%global vfs_modules    vfs_dfs_samba4,vfs_fake_dfq
%global samba_modules  %{idmap_modules},%{pdb_modules},%{auth_modules},%{vfs_modules}

# Change to 1 to enable these
%bcond ceph 1
%bcond pmda 0
%bcond glusterfs 0

# Why this macro magically disappeared is beyond me - 251
%{?python3_sitearch: %global python3_sitearch %{python3_sitearch}}

Name:           samba
Version:        4.23.2
Release:        %autorelease
Summary:        Server and Client software to interoperate with Windows machines
License:        GPL-3.0-or-later
URL:            https://www.samba.org
VCS:            git:https://git.samba.org/samba.git
#!RemoteAsset:  sha256:2de330647e1486683597e261285d04a9b7514ab5c7da27711736e22c7f2b9c2e
Source0:        https://download.samba.org/pub/samba/stable/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:c514f0a0aa41c351e08eb05925e10653546c4f3f582181ba851dd81e470cb439
Source1:        https://download.samba.org/pub/samba/stable/%{name}-%{version}.tar.asc
Source2:        samba-systemd.sysusers
Source3:        samba-winbind-systemd.sysusers
Source4:        samba-usershares-systemd.sysusers
Source5:        samba.tmpfiles
BuildSystem:    autotools

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --disable-rpath-install
BuildOption(conf):  --with-piddir=/run/samba
BuildOption(conf):  --prefix=%{_prefix}
BuildOption(conf):  --localstatedir=%{_localstatedir}
BuildOption(conf):  --sysconfdir=%{_sysconfdir}
BuildOption(conf):  --libdir=%{_libdir}
BuildOption(conf):  --libexecdir=%{_libdir}
BuildOption(conf):  --with-cachedir=%{_localstatedir}/lib/samba
BuildOption(conf):  --with-lockdir=%{_localstatedir}/lib/samba/lock
BuildOption(conf):  --with-logfilebase=%{_localstatedir}/log/samba
BuildOption(conf):  --with-modulesdir=%{_libdir}/samba
BuildOption(conf):  --with-shared-modules=%{samba_modules}
BuildOption(conf):  --bundled-libraries="!popt,!talloc,!pytalloc,!pytalloc-util,!tevent,!pytevent,!tdb,!pytdb"
BuildOption(conf):  --private-libraries="!ldb"
BuildOption(conf):  --with-ads
BuildOption(conf):  --with-ldap
BuildOption(conf):  --with-winbind
BuildOption(conf):  --with-acl-support
BuildOption(conf):  --with-systemd
BuildOption(conf):  --systemd-install-services
BuildOption(conf):  --with-pam
BuildOption(conf):  --with-pammodulesdir=%{_libdir}/security
BuildOption(conf):  --enable-fhs
BuildOption(conf):  --with-profiling-data
%if %{without glusterfs}
BuildOption(conf):  --disable-glusterfs
%endif
%if %{without ceph}
BuildOption(conf):  --without-cephfs
%endif
BuildOption(check):  TEST_OPTIONS=--quick

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  flex
BuildRequires:  pkgconfig(tdb)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  pkgconfig(tevent)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libaio)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libxcrypt)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  libxslt
BuildRequires:  pkgconfig(lmdb)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(pam)
BuildRequires:  perl(Parse::Yapp)
BuildRequires:  perl(JSON)
BuildRequires:  pkgconfig(popt)
BuildRequires:  python3-cryptography
BuildRequires:  python3-devel
BuildRequires:  python3-dnspython
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-markdown
BuildRequires:  python3-tdb
BuildRequires:  python3-talloc-devel
BuildRequires:  python3-tevent
BuildRequires:  pkgconfig(readline)
BuildRequires:  rpcgen
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  xfsprogs-devel
BuildRequires:  pkgconfig(zlib)
%if %{with glusterfs}
BuildRequires:  glusterfs-devel
%endif
%if %{with ceph}
BuildRequires:  pkgconfig(cephfs)
BuildRequires:  ceph-devel
%endif
BuildRequires:  pkgconfig(liburing)
%if %{with pmda}
BuildRequires:  pcp-devel
%endif

BuildRequires:  docbook-style-dsssl
BuildRequires:  doxygen

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Samba is the standard Windows interoperability suite of programs for Linux and
Unix.

%package        client
Summary:        Samba client programs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    client
This package provides some SMB/CIFS clients to complement the built-in SMB/CIFS
filesystem in Linux. These clients allow access of SMB/CIFS shares and printing
to SMB/CIFS printers.

%package        devel
Summary:        Developer tools for Samba libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libwbclient%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files for the libraries needed to develop
programs that link against the SMB, RPC and other libraries in the Samba suite.

%package        libs
Summary:        Libraries used by both Samba servers and clients

%description    libs
This package contains internal libraries needed by the SMB/CIFS clients.

%package        ad-dc
Summary:        Samba AD Domain Controller
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-client%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       ldb%{?_isa} = %{version}-%{release}
Requires:       python3-ldb
Requires:       python3-%{name} = %{version}-%{release}

%description    ad-dc
This package provides AD Domain Controller functionality

%package        winbind
Summary:        Samba winbind
Requires:       %{name}-client%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    winbind
This package provides the winbind NSS library, and some client tools.

Winbind enables Linux to be a full member in Windows domains and to use
Windows user and group accounts on Linux.

%package     -n python-%{name}
Summary:        Samba Python libraries
Provides:       python3-%{name}
%python_provide python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-client%{?_isa} = %{version}-%{release}
Requires:       python3-ldb
Requires:       python3-talloc
Requires:       python3-tdb
Requires:       python3-tevent

%description -n python-%{name}
This package contains the Python libraries needed by programs that use SMB,
RPC and other Samba provided protocols in Python programs.

%package     -n libwbclient
Summary:        The winbind client library

%description -n libwbclient
This package contains the winbind client library from the Samba suite.

%package     -n ldb
Summary:        A schema-less, ldap like, API and database
License:        LGPL-3.0-or-later

%description -n ldb
An extensible library that implements an LDAP like API to access remote LDAP
servers, or use local tdb databases.

%package     -n python-ldb
Summary:        Ldb Python bindings
License:        LGPL-3.0-or-later
Provides:       python3-ldb
%python_provide python3-ldb
Requires:       ldb%{?_isa} = %{version}-%{release}

%description -n python-ldb
Python bindings for the LDB library

%if %{with ceph}
%package        cephfs
Summary:        Samba SMB gateway for CephFS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    cephfs
Expose CephFS (and RADOS) as SMB/CIFS shares directly via libcephfs,
without an intermediate kernel mount.
%endif

%conf -p
# https://gitlab.com/ita1024/waf/-/issues/2472
export PYTHONARCHDIR=%{python3_sitearch}

%build
# Do not use %%make_build, make is just a wrapper around waf in Samba
%{__make} %{?_smp_mflags} VERBOSE=1

%install
install -d -m 0755 %{buildroot}%{_libdir}/security
install -d -m 0755 %{buildroot}/var/lib/samba
install -d -m 0755 %{buildroot}/var/lib/samba/certs
install -d -m 0755 %{buildroot}/var/lib/samba/drivers
install -d -m 0755 %{buildroot}/var/lib/samba/lock
install -d -m 0755 %{buildroot}/var/lib/samba/private
install -d -m 0755 %{buildroot}/var/lib/samba/private/certs
install -d -m 0755 %{buildroot}/var/lib/samba/scripts
install -d -m 0755 %{buildroot}/var/lib/samba/sysvol
install -d -m 0755 %{buildroot}/var/lib/samba/usershares
install -d -m 0755 %{buildroot}/var/lib/samba/winbindd_privileged
install -d -m 0755 %{buildroot}/var/log/samba/old
install -d -m 0755 %{buildroot}/run/samba
install -d -m 0755 %{buildroot}/run/winbindd
install -d -m 0755 %{buildroot}/%{_libdir}/samba
install -d -m 0755 %{buildroot}/%{_libdir}/samba/ldb
install -d -m 0755 %{buildroot}/%{_libdir}/pkgconfig
install -d -m 0755 %{buildroot}%{_sysconfdir}/pam.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/security

# Do not use %%make_install, make is just a wrapper around waf in Samba
%{__make} %{?_smp_mflags} VERBOSE=1 install DESTDIR=%{buildroot} CONFIGDIR=%{_sysconfdir}/samba

install -m 0644 examples/smb.conf.default %{buildroot}%{_sysconfdir}/samba/smb.conf
echo "127.0.0.1 localhost" > %{buildroot}%{_sysconfdir}/samba/lmhosts

install -d -m 0755 %{buildroot}%{_sysconfdir}/security
install -m 0644 examples/pam_winbind/pam_winbind.conf %{buildroot}%{_sysconfdir}/security/pam_winbind.conf

install -d -m 0755 %{buildroot}%{_sysconfdir}/openldap/schema
install -m644 examples/LDAP/samba.schema %{buildroot}%{_sysconfdir}/openldap/schema/samba.schema

install -m 0644 -Dp %{SOURCE2} %{buildroot}%{_sysusersdir}/samba.conf
install -m 0644 -Dp %{SOURCE3} %{buildroot}%{_sysusersdir}/samba-winbind.conf
install -m 0644 -Dp %{SOURCE4} %{buildroot}%{_sysusersdir}/samba-usershares.conf

install -d -m 0755 %{buildroot}%{_tmpfilesdir}
install -D %{SOURCE5} %{buildroot}%{_tmpfilesdir}/samba.conf

install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig
install -m 0644 packaging/systemd/samba.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/samba

%if %{without glusterfs}
rm -f %{buildroot}%{_mandir}/man8/vfs_glusterfs.8*
%endif

# TODO: Fix check.
%check

%pre
%sysusers_create_package %{name} %{SOURCE2}
%sysusers_create_package %{name}-usershares %{SOURCE4}

%pre winbind
%sysusers_create_package %{name}-winbind %{SOURCE3}

%post
%tmpfiles_create_package %{name} %{SOURCE5}
%systemd_post samba-bgqd.service
%systemd_post smb.service
%systemd_post nmb.service

%preun
%systemd_preun samba-bgqd.service
%systemd_preun smb.service
%systemd_preun nmb.service

%postun
%systemd_postun_with_restart samba-bgqd.service
%systemd_postun_with_restart smb.service
%systemd_postun_with_restart nmb.service

%files
%license COPYING
%doc examples/autofs examples/LDAP examples/misc
%doc examples/printer-accounting examples/printing
%doc README.md WHATSNEW.txt
%{_bindir}/smbstatus
%{_bindir}/net
%{_bindir}/pdbedit
%{_bindir}/profiles
%{_bindir}/samba-log-parser
%{_bindir}/smbcontrol
%{_bindir}/smbpasswd
%{_bindir}/testparm
%{_bindir}/gentest
%{_bindir}/locktest
%{_bindir}/masktest
%{_bindir}/ndrdump
%{_bindir}/smbtorture
%{_bindir}/samba-tool
%{_sbindir}/eventlogadm
%{_sbindir}/nmbd
%{_sbindir}/smbd
%{_sbindir}/samba-gpupdate
%{_libdir}/samba/libHDB-SAMBA4-private-samba.so
%{_libdir}/samba/libdfs-server-ad-private-samba.so
%dir %{_libdir}/samba/auth
%{_libdir}/samba/auth/unix.so
%dir %{_libdir}/samba/vfs
%{_libdir}/samba/vfs/acl_tdb.so
%{_libdir}/samba/vfs/acl_xattr.so
%{_libdir}/samba/vfs/aio_fork.so
%{_libdir}/samba/vfs/aio_pthread.so
%{_libdir}/samba/vfs/audit.so
%{_libdir}/samba/vfs/btrfs.so
%{_libdir}/samba/vfs/cap.so
%{_libdir}/samba/vfs/catia.so
%{_libdir}/samba/vfs/commit.so
%{_libdir}/samba/vfs/crossrename.so
%{_libdir}/samba/vfs/default_quota.so
%{_libdir}/samba/vfs/dfs_samba4.so
%{_libdir}/samba/vfs/dirsort.so
%{_libdir}/samba/vfs/expand_msdfs.so
%{_libdir}/samba/vfs/extd_audit.so
%{_libdir}/samba/vfs/fake_perms.so
%{_libdir}/samba/vfs/fileid.so
%{_libdir}/samba/vfs/fruit.so
%{_libdir}/samba/vfs/full_audit.so
%{_libdir}/samba/vfs/gpfs.so
# TODO: Help! We don't have glusterfs but why is this here? - 251
%{_libdir}/samba/vfs/glusterfs_fuse.so
%{_libdir}/samba/vfs/linux_xfs_sgid.so
%{_libdir}/samba/vfs/media_harmony.so
%{_libdir}/samba/vfs/offline.so
%{_libdir}/samba/vfs/preopen.so
%{_libdir}/samba/vfs/readahead.so
%{_libdir}/samba/vfs/readonly.so
%{_libdir}/samba/vfs/recycle.so
%{_libdir}/samba/vfs/shadow_copy.so
%{_libdir}/samba/vfs/shadow_copy2.so
%{_libdir}/samba/vfs/shell_snap.so
%{_libdir}/samba/vfs/snapper.so
%{_libdir}/samba/vfs/streams_depot.so
%{_libdir}/samba/vfs/streams_xattr.so
%{_libdir}/samba/vfs/syncops.so
%{_libdir}/samba/vfs/time_audit.so
%{_libdir}/samba/vfs/unityed_media.so
%{_libdir}/samba/vfs/virusfilter.so
%{_libdir}/samba/vfs/widelinks.so
%{_libdir}/samba/vfs/worm.so
%{_libdir}/samba/vfs/xattr_tdb.so
%{_libdir}/samba/vfs/io_uring.so
%{_libdir}/samba/libasn1-private-samba.so
%{_libdir}/samba/libcom-err-private-samba.so
%{_libdir}/samba/libgss-preauth-private-samba.so
%{_libdir}/samba/libgssapi-private-samba.so
%{_libdir}/samba/libhcrypto-private-samba.so
%{_libdir}/samba/libhdb-private-samba.so
%{_libdir}/samba/libheimbase-private-samba.so
%{_libdir}/samba/libheimntlm-private-samba.so
%{_libdir}/samba/libhx509-private-samba.so
%{_libdir}/samba/libkdc-private-samba.so
%{_libdir}/samba/libkrb5-private-samba.so
%{_libdir}/samba/libroken-private-samba.so
%{_libdir}/samba/libwind-private-samba.so
%{_libdir}/samba/samba-dcerpcd
%{_libdir}/samba/rpcd_classic
%{_libdir}/samba/rpcd_epmapper
%{_libdir}/samba/rpcd_fsrvp
%{_libdir}/samba/rpcd_lsad
%{_libdir}/samba/rpcd_mdssvc
%{_libdir}/samba/rpcd_spoolss
%{_libdir}/samba/rpcd_winreg
%{_libdir}/samba/samba-bgqd
%dir %{_datadir}/samba
%dir %{_datadir}/samba/mdssvc
%{_datadir}/samba/mdssvc/elasticsearch_mappings.json
%{_unitdir}/nmb.service
%{_unitdir}/smb.service
%{_unitdir}/samba-bgqd.service
%dir %{_sysconfdir}/openldap/schema
%config %{_sysconfdir}/openldap/schema/samba.schema
%attr(775,root,printadmin) %dir /var/lib/samba/drivers
%{_tmpfilesdir}/samba.conf
%{_sysusersdir}/samba.conf
%{_sysusersdir}/samba-usershares.conf
%attr(0700,root,root) %dir /var/log/samba
%attr(0700,root,root) %dir /var/log/samba/old
%ghost %dir /run/samba
%ghost %dir /run/winbindd
%dir /var/lib/samba
%dir /var/lib/samba/certs
%attr(700,root,root) %dir /var/lib/samba/private
%attr(700,root,root) %dir /var/lib/samba/private/certs
%dir /var/lib/samba/lock
%attr(755,root,root) %dir %{_sysconfdir}/samba
%config(noreplace) %{_sysconfdir}/samba/smb.conf
%config(noreplace) %{_sysconfdir}/samba/lmhosts
%config(noreplace) %{_sysconfdir}/sysconfig/samba
%{_datadir}/locale/*/LC_MESSAGES/net.mo

%files client
%doc source3/client/README.smbspool
%{_bindir}/cifsdd
%{_bindir}/dbwrap_tool
%{_bindir}/dumpmscat
%{_bindir}/mvxattr
%{_bindir}/mdsearch
%{_bindir}/nmblookup
%{_bindir}/oLschema2ldif
%{_bindir}/regdiff
%{_bindir}/regpatch
%{_bindir}/regshell
%{_bindir}/regtree
%{_bindir}/rpcclient
%{_bindir}/samba-regedit
%{_bindir}/sharesec
%{_bindir}/smbcacls
%{_bindir}/smbclient
%{_bindir}/smbcquotas
%{_bindir}/smbget
%{_bindir}/smbspool
%{_bindir}/smbtar
%{_bindir}/smbtree
%{_bindir}/wspsearch
%{_libdir}/samba/smbspool_krb5_wrapper

%files devel
%{_includedir}/samba-4.0/charset.h
%{_includedir}/samba-4.0/core/doserr.h
%{_includedir}/samba-4.0/core/error.h
%{_includedir}/samba-4.0/core/hresult.h
%{_includedir}/samba-4.0/core/ntstatus.h
%{_includedir}/samba-4.0/core/ntstatus_gen.h
%{_includedir}/samba-4.0/core/werror.h
%{_includedir}/samba-4.0/core/werror_gen.h
%{_includedir}/samba-4.0/credentials.h
%{_includedir}/samba-4.0/dcerpc.h
%{_includedir}/samba-4.0/dcerpc_server.h
%{_includedir}/samba-4.0/dcesrv_core.h
%{_includedir}/samba-4.0/domain_credentials.h
%{_includedir}/samba-4.0/gen_ndr/atsvc.h
%{_includedir}/samba-4.0/gen_ndr/auth.h
%{_includedir}/samba-4.0/gen_ndr/claims.h
%{_includedir}/samba-4.0/gen_ndr/dcerpc.h
%{_includedir}/samba-4.0/gen_ndr/krb5pac.h
%{_includedir}/samba-4.0/gen_ndr/lsa.h
%{_includedir}/samba-4.0/gen_ndr/misc.h
%{_includedir}/samba-4.0/gen_ndr/nbt.h
%{_includedir}/samba-4.0/gen_ndr/drsblobs.h
%{_includedir}/samba-4.0/gen_ndr/drsuapi.h
%{_includedir}/samba-4.0/gen_ndr/ndr_drsblobs.h
%{_includedir}/samba-4.0/gen_ndr/ndr_drsuapi.h
%{_includedir}/samba-4.0/gen_ndr/ndr_atsvc.h
%{_includedir}/samba-4.0/gen_ndr/ndr_dcerpc.h
%{_includedir}/samba-4.0/gen_ndr/ndr_krb5pac.h
%{_includedir}/samba-4.0/gen_ndr/ndr_misc.h
%{_includedir}/samba-4.0/gen_ndr/ndr_nbt.h
%{_includedir}/samba-4.0/gen_ndr/ndr_samr.h
%{_includedir}/samba-4.0/gen_ndr/ndr_samr_c.h
%{_includedir}/samba-4.0/gen_ndr/ndr_svcctl.h
%{_includedir}/samba-4.0/gen_ndr/ndr_svcctl_c.h
%{_includedir}/samba-4.0/gen_ndr/netlogon.h
%{_includedir}/samba-4.0/gen_ndr/samr.h
%{_includedir}/samba-4.0/gen_ndr/security.h
%{_includedir}/samba-4.0/gen_ndr/server_id.h
%{_includedir}/samba-4.0/gen_ndr/svcctl.h
%{_includedir}/samba-4.0/ldb_wrap.h
%{_includedir}/samba-4.0/lookup_sid.h
%{_includedir}/samba-4.0/machine_sid.h
%{_includedir}/samba-4.0/ndr.h
%dir %{_includedir}/samba-4.0/ndr
%{_includedir}/samba-4.0/ndr/ndr_dcerpc.h
%{_includedir}/samba-4.0/ndr/ndr_drsblobs.h
%{_includedir}/samba-4.0/ndr/ndr_drsuapi.h
%{_includedir}/samba-4.0/ndr/ndr_krb5pac.h
%{_includedir}/samba-4.0/ndr/ndr_svcctl.h
%{_includedir}/samba-4.0/ndr/ndr_nbt.h
%{_includedir}/samba-4.0/param.h
%{_includedir}/samba-4.0/passdb.h
%{_includedir}/samba-4.0/policy.h
%{_includedir}/samba-4.0/rpc_common.h
%{_includedir}/samba-4.0/samba/session.h
%{_includedir}/samba-4.0/samba/version.h
%{_includedir}/samba-4.0/share.h
%{_includedir}/samba-4.0/smb2_lease_struct.h
%{_includedir}/samba-4.0/smb3posix.h
%{_includedir}/samba-4.0/smbconf.h
%{_includedir}/samba-4.0/smb_ldap.h
%{_includedir}/samba-4.0/smbldap.h
%{_includedir}/samba-4.0/tdr.h
%{_includedir}/samba-4.0/tsocket.h
%{_includedir}/samba-4.0/tsocket_internal.h
%dir %{_includedir}/samba-4.0/util
%{_includedir}/samba-4.0/util/attr.h
%{_includedir}/samba-4.0/util/blocking.h
%{_includedir}/samba-4.0/util/data_blob.h
%{_includedir}/samba-4.0/util/debug.h
%{_includedir}/samba-4.0/util/discard.h
%{_includedir}/samba-4.0/util/fault.h
%{_includedir}/samba-4.0/util/genrand.h
%{_includedir}/samba-4.0/util/idtree.h
%{_includedir}/samba-4.0/util/idtree_random.h
%{_includedir}/samba-4.0/util/signal.h
%{_includedir}/samba-4.0/util/substitute.h
%{_includedir}/samba-4.0/util/tevent_ntstatus.h
%{_includedir}/samba-4.0/util/tevent_unix.h
%{_includedir}/samba-4.0/util/tevent_werror.h
%{_includedir}/samba-4.0/util/time.h
%{_includedir}/samba-4.0/util/tfork.h
%{_includedir}/samba-4.0/util_ldb.h
%{_libdir}/libdcerpc-samr.so
%{_libdir}/libdcerpc-server.so
%{_libdir}/libdcerpc-binding.so
%{_libdir}/libdcerpc-server-core.so
%{_libdir}/libdcerpc.so
%{_libdir}/libndr-krb5pac.so
%{_libdir}/libndr-nbt.so
%{_libdir}/libndr-standard.so
%{_libdir}/libndr.so
%{_libdir}/libsamba-credentials.so
%{_libdir}/libsamba-hostconfig.so
%{_libdir}/libsamba-errors.so
%{_libdir}/libsamba-util.so
%{_libdir}/libsamdb.so
%{_libdir}/libsmbconf.so
%{_libdir}/libtevent-util.so
%{_libdir}/pkgconfig/dcerpc.pc
%{_libdir}/pkgconfig/dcerpc_samr.pc
%{_libdir}/pkgconfig/dcerpc_server.pc
%{_libdir}/pkgconfig/ndr.pc
%{_libdir}/pkgconfig/ndr_krb5pac.pc
%{_libdir}/pkgconfig/ndr_nbt.pc
%{_libdir}/pkgconfig/ndr_standard.pc
%{_libdir}/pkgconfig/samba-credentials.pc
%{_libdir}/pkgconfig/samba-hostconfig.pc
%{_libdir}/pkgconfig/samba-policy.pc
%{_libdir}/pkgconfig/samba-util.pc
%{_libdir}/pkgconfig/samdb.pc
%{_libdir}/libsamba-policy.so
%{_libdir}/libsamba-passdb.so
%{_libdir}/libsmbldap.so
%{_includedir}/samba-4.0/libsmbclient.h
%{_includedir}/samba-4.0/netapi.h
%{_libdir}/libnetapi.so
%{_libdir}/pkgconfig/netapi.pc
%{_libdir}/libsmbclient.so
%{_libdir}/pkgconfig/smbclient.pc

%files libs
%{_libdir}/samba/libcmdline-private-samba.so
%{_libdir}/samba/libreplace-private-samba.so
%dir %{_libdir}/samba/ldb
%dir %{_libdir}/samba/pdb
%{_libdir}/samba/pdb/ldapsam.so
%{_libdir}/samba/pdb/smbpasswd.so
%{_libdir}/samba/pdb/tdbsam.so
# samba libs
%{_libdir}/libdcerpc-samr.so.*
%{_libdir}/samba/libLIBWBCLIENT-OLD-private-samba.so
%{_libdir}/samba/libauth-unix-token-private-samba.so
%{_libdir}/samba/libdcerpc-samba4-private-samba.so
%{_libdir}/samba/libdnsserver-common-private-samba.so
%{_libdir}/samba/libshares-private-samba.so
%{_libdir}/samba/libsmbpasswdparser-private-samba.so
%{_libdir}/samba/libxattr-tdb-private-samba.so
%{_libdir}/samba/libREG-FULL-private-samba.so
%{_libdir}/samba/libRPC-SERVER-LOOP-private-samba.so
%{_libdir}/samba/libRPC-WORKER-private-samba.so
# client libs
%{_libdir}/libdcerpc-binding.so.*
%{_libdir}/libdcerpc-server-core.so.*
%{_libdir}/libdcerpc.so.*
%{_libdir}/libndr-krb5pac.so.*
%{_libdir}/libndr-nbt.so.*
%{_libdir}/libndr-standard.so.*
%{_libdir}/libndr.so.*
%{_libdir}/libsamba-credentials.so.*
%{_libdir}/libsamba-errors.so.*
%{_libdir}/libsamba-hostconfig.so.*
%{_libdir}/libsamba-passdb.so.*
%{_libdir}/libsamba-util.so.*
%{_libdir}/libsamdb.so.*
%{_libdir}/libsmbconf.so.*
%{_libdir}/libsmbldap.so.*
%{_libdir}/libtevent-util.so.*
%dir %{_libdir}/samba
%{_libdir}/samba/libCHARSET3-private-samba.so
%{_libdir}/samba/libMESSAGING-SEND-private-samba.so
%{_libdir}/samba/libMESSAGING-private-samba.so
%{_libdir}/samba/libaddns-private-samba.so
%{_libdir}/samba/libads-private-samba.so
%{_libdir}/samba/libasn1util-private-samba.so
%{_libdir}/samba/libauth-private-samba.so
%{_libdir}/samba/libauthkrb5-private-samba.so
%{_libdir}/samba/libcli-cldap-private-samba.so
%{_libdir}/samba/libcli-ldap-common-private-samba.so
%{_libdir}/samba/libcli-ldap-private-samba.so
%{_libdir}/samba/libcli-nbt-private-samba.so
%{_libdir}/samba/libcli-smb-common-private-samba.so
%{_libdir}/samba/libcli-spoolss-private-samba.so
%{_libdir}/samba/libcliauth-private-samba.so
%{_libdir}/samba/libclidns-private-samba.so
%{_libdir}/samba/libcluster-private-samba.so
%{_libdir}/samba/libcmdline-contexts-private-samba.so
%{_libdir}/samba/libcommon-auth-private-samba.so
%{_libdir}/samba/libdbwrap-private-samba.so
%{_libdir}/samba/libdcerpc-pkt-auth-private-samba.so
%{_libdir}/samba/libdcerpc-samba-private-samba.so
%{_libdir}/samba/libevents-private-samba.so
%{_libdir}/samba/libflag-mapping-private-samba.so
%{_libdir}/samba/libgenrand-private-samba.so
%{_libdir}/samba/libgensec-private-samba.so
%{_libdir}/samba/libgpext-private-samba.so
%{_libdir}/samba/libgpo-private-samba.so
%{_libdir}/samba/libgse-private-samba.so
%{_libdir}/samba/libhttp-private-samba.so
%{_libdir}/samba/libinterfaces-private-samba.so
%{_libdir}/samba/libiov-buf-private-samba.so
%{_libdir}/samba/libkrb5samba-private-samba.so
%{_libdir}/samba/libldbsamba-private-samba.so
%{_libdir}/samba/liblibcli-lsa3-private-samba.so
%{_libdir}/samba/liblibcli-netlogon3-private-samba.so
%{_libdir}/samba/liblibsmb-private-samba.so
%{_libdir}/samba/libmessages-dgm-private-samba.so
%{_libdir}/samba/libmessages-util-private-samba.so
%{_libdir}/samba/libmscat-private-samba.so
%{_libdir}/samba/libmsghdr-private-samba.so
%{_libdir}/samba/libmsrpc3-private-samba.so
%{_libdir}/samba/libndr-samba-private-samba.so
%{_libdir}/samba/libndr-samba4-private-samba.so
%{_libdir}/samba/libnet-keytab-private-samba.so
%{_libdir}/samba/libnetif-private-samba.so
%{_libdir}/samba/libnpa-tstream-private-samba.so
%{_libdir}/samba/libposix-eadb-private-samba.so
%{_libdir}/samba/libprinter-driver-private-samba.so
%{_libdir}/samba/libprinting-migrate-private-samba.so
%{_libdir}/samba/libquic-private-samba.so
%{_libdir}/samba/libregistry-private-samba.so
%{_libdir}/samba/libsamba-cluster-support-private-samba.so
%{_libdir}/samba/libsamba-debug-private-samba.so
%{_libdir}/samba/libsamba-modules-private-samba.so
%{_libdir}/samba/libsamba-security-private-samba.so
%{_libdir}/samba/libsamba-security-trusts-private-samba.so
%{_libdir}/samba/libsamba-sockets-private-samba.so
%{_libdir}/samba/libsamba3-util-private-samba.so
%{_libdir}/samba/libsamdb-common-private-samba.so
%{_libdir}/samba/libsecrets3-private-samba.so
%{_libdir}/samba/libserver-id-db-private-samba.so
%{_libdir}/samba/libserver-role-private-samba.so
%{_libdir}/samba/libsmbclient-raw-private-samba.so
%{_libdir}/samba/libsmbd-base-private-samba.so
%{_libdir}/samba/libsmbd-shim-private-samba.so
%{_libdir}/samba/libsmbldaphelper-private-samba.so
%{_libdir}/samba/libstable-sort-private-samba.so
%{_libdir}/samba/libsys-rw-private-samba.so
%{_libdir}/samba/libsocket-blocking-private-samba.so
%{_libdir}/samba/libtalloc-report-printf-private-samba.so
%{_libdir}/samba/libtalloc-report-private-samba.so
%{_libdir}/samba/libtdb-wrap-private-samba.so
%{_libdir}/samba/libtime-basic-private-samba.so
%{_libdir}/samba/libtorture-private-samba.so
%{_libdir}/samba/libutil-crypt-private-samba.so
%{_libdir}/samba/libutil-reg-private-samba.so
%{_libdir}/samba/libutil-setid-private-samba.so
%{_libdir}/samba/libutil-tdb-private-samba.so
%{_libdir}/samba/libldb-*.so
%{_libdir}/samba/libngtcp2-crypto-gnutls-private-samba.so
%{_libdir}/samba/libngtcp2-private-samba.so
# dc libs
%{_libdir}/libsamba-policy.so.*
%{_libdir}/samba/libauth4-private-samba.so
%{_libdir}/samba/libsamba-net-private-samba.so
%{_libdir}/samba/libdb-glue-private-samba.so
%{_libdir}/samba/libpac-private-samba.so
%{_libdir}/samba/libprocess-model-private-samba.so
%{_libdir}/samba/libservice-private-samba.so
%dir %{_libdir}/samba/process_model
%{_libdir}/samba/process_model/prefork.so
%{_libdir}/samba/process_model/standard.so
%dir %{_libdir}/samba/service
%{_libdir}/samba/service/cldap.so
%{_libdir}/samba/service/dcerpc.so
%{_libdir}/samba/service/dns.so
%{_libdir}/samba/service/dns_update.so
%{_libdir}/samba/service/drepl.so
%{_libdir}/samba/service/ft_scanner.so
%{_libdir}/samba/service/kcc.so
%{_libdir}/samba/service/kdc.so
%{_libdir}/samba/service/ldap.so
%{_libdir}/samba/service/nbtd.so
%{_libdir}/samba/service/ntp_signd.so
%{_libdir}/samba/service/s3fs.so
%{_libdir}/samba/service/winbindd.so
%{_libdir}/samba/service/wrepl.so
%{_libdir}/libdcerpc-server.so.*
%{_libdir}/samba/libad-claims-private-samba.so
%{_libdir}/samba/libauthn-policy-util-private-samba.so
%{_libdir}/samba/libdsdb-garbage-collect-tombstones-private-samba.so
%{_libdir}/samba/libscavenge-dns-records-private-samba.so
# libnetapi libs
%{_libdir}/libnetapi.so.*
# libsmbclient libs
%{_libdir}/libsmbclient.so.*
# test libs
%{_libdir}/samba/libdlz-bind9-for-torture-private-samba.so
%{_libdir}/samba/libdsdb-module-private-samba.so

%files ad-dc
%{_unitdir}/samba.service
%{_sbindir}/samba
%{_sbindir}/samba_dnsupdate
%{_sbindir}/samba_downgrade_db
%{_sbindir}/samba_kcc
%{_sbindir}/samba_spnupdate
%{_sbindir}/samba_upgradedns
%{_libdir}/samba/auth/samba4.so
%dir %{_libdir}/samba/gensec
%{_libdir}/samba/gensec/krb5.so
%{_libdir}/samba/ldb/acl.so
%{_libdir}/samba/ldb/aclread.so
%{_libdir}/samba/ldb/anr.so
%{_libdir}/samba/ldb/audit_log.so
%{_libdir}/samba/ldb/count_attrs.so
%{_libdir}/samba/ldb/descriptor.so
%{_libdir}/samba/ldb/dirsync.so
%{_libdir}/samba/ldb/dns_notify.so
%{_libdir}/samba/ldb/dsdb_notification.so
%{_libdir}/samba/ldb/encrypted_secrets.so
%{_libdir}/samba/ldb/extended_dn_in.so
%{_libdir}/samba/ldb/extended_dn_out.so
%{_libdir}/samba/ldb/extended_dn_store.so
%{_libdir}/samba/ldb/group_audit_log.so
%{_libdir}/samba/ldb/instancetype.so
%{_libdir}/samba/ldb/lazy_commit.so
%{_libdir}/samba/ldb/linked_attributes.so
%{_libdir}/samba/ldb/new_partition.so
%{_libdir}/samba/ldb/objectclass.so
%{_libdir}/samba/ldb/objectclass_attrs.so
%{_libdir}/samba/ldb/objectguid.so
%{_libdir}/samba/ldb/operational.so
%{_libdir}/samba/ldb/paged_results.so
%{_libdir}/samba/ldb/partition.so
%{_libdir}/samba/ldb/password_hash.so
%{_libdir}/samba/ldb/ranged_results.so
%{_libdir}/samba/ldb/repl_meta_data.so
%{_libdir}/samba/ldb/resolve_oids.so
%{_libdir}/samba/ldb/rootdse.so
%{_libdir}/samba/ldb/samba3sam.so
%{_libdir}/samba/ldb/samba3sid.so
%{_libdir}/samba/ldb/samba_dsdb.so
%{_libdir}/samba/ldb/samba_secrets.so
%{_libdir}/samba/ldb/samldb.so
%{_libdir}/samba/ldb/schema_data.so
%{_libdir}/samba/ldb/schema_load.so
%{_libdir}/samba/ldb/secrets_tdb_sync.so
%{_libdir}/samba/ldb/show_deleted.so
%{_libdir}/samba/ldb/subtree_delete.so
%{_libdir}/samba/ldb/subtree_rename.so
%{_libdir}/samba/ldb/tombstone_reanimate.so
%{_libdir}/samba/ldb/trust_notify.so
%{_libdir}/samba/ldb/unique_object_sids.so
%{_libdir}/samba/ldb/update_keytab.so
%{_libdir}/samba/ldb/vlv.so
%{_libdir}/samba/ldb/wins_ldb.so
%{_libdir}/samba/vfs/posix_eadb.so
%dir %{_libdir}/samba/bind9
%{_libdir}/samba/bind9/dlz_bind9_10.so
%{_libdir}/samba/bind9/dlz_bind9_11.so
%{_libdir}/samba/bind9/dlz_bind9_12.so
%{_libdir}/samba/bind9/dlz_bind9_14.so
%{_libdir}/samba/bind9/dlz_bind9_16.so
%{_libdir}/samba/bind9/dlz_bind9_18.so
%attr(770,root,named) %dir /var/lib/samba/bind-dns
%dir /var/lib/samba/sysvol
%dir %{_datadir}/samba/admx
%{_datadir}/samba/admx/GNOME_Settings.admx
%{_datadir}/samba/admx/samba.admx
%dir %{_datadir}/samba/admx/en-US
%{_datadir}/samba/admx/en-US/GNOME_Settings.adml
%{_datadir}/samba/admx/en-US/samba.adml
%dir %{_datadir}/samba/admx/ru-RU
%{_datadir}/samba/admx/ru-RU/GNOME_Settings.adml
%{_datadir}/samba/setup

%files -n python-%{name}
%dir %{python3_sitearch}/samba/
%{python3_sitearch}/samba/*
%{_libdir}/samba/libsamba-net-join.cpython*.so
%{_libdir}/samba/libsamba-python.cpython*.so

%files winbind
%{_libdir}/samba/idmap
%{_libdir}/samba/nss_info
%{_libdir}/samba/libnss-info-private-samba.so
%{_libdir}/samba/libidmap-private-samba.so
%{_sbindir}/winbindd
%{_sysusersdir}/samba-winbind.conf
%attr(750,root,wbpriv) %dir /var/lib/samba/winbindd_privileged
%{_unitdir}/winbind.service
%{_bindir}/ntlm_auth
%{_bindir}/wbinfo
%dir %{_libdir}/samba/krb5
%{_libdir}/samba/krb5/winbind_krb5_locator.so
%{_libdir}/samba/krb5/async_dns_krb5_locator.so
%{_libdir}/libnss_winbind.so*
%{_libdir}/libnss_wins.so*
%{_libdir}/security/pam_winbind.so
%config(noreplace) %{_sysconfdir}/security/pam_winbind.conf
%{_datadir}/locale/*/LC_MESSAGES/pam_winbind.mo

%files -n libwbclient
%{_libdir}/libwbclient.so.*
%{_includedir}/samba-4.0/wbclient.h
%{_libdir}/libwbclient.so
%{_libdir}/pkgconfig/wbclient.pc

%files -n ldb
%{_bindir}/ldbadd
%{_bindir}/ldbdel
%{_bindir}/ldbedit
%{_bindir}/ldbmodify
%{_bindir}/ldbrename
%{_bindir}/ldbsearch
%{_libdir}/libldb.so
%{_libdir}/libldb.so.*
%{_libdir}/pkgconfig/ldb.pc
%dir %{_libdir}/samba
%{_libdir}/samba/libldb-key-value-private-samba.so
%{_libdir}/samba/libldb-tdb-err-map-private-samba.so
%{_libdir}/samba/libldb-tdb-int-private-samba.so
%{_libdir}/samba/libldb-mdb-int-private-samba.so
%dir %{_libdir}/samba/ldb
%{_libdir}/samba/ldb/asq.so
%{_libdir}/samba/ldb/ldb.so
%{_libdir}/samba/ldb/mdb.so
%{_libdir}/samba/ldb/paged_searches.so
%{_libdir}/samba/ldb/rdn_name.so
%{_libdir}/samba/ldb/sample.so
%{_libdir}/samba/ldb/server_sort.so
%{_libdir}/samba/ldb/skel.so
%{_libdir}/samba/ldb/tdb.so
%{_libdir}/samba/ldb/ldbsamba_extensions.so
%{_libdir}/samba/ldb/ildap.so
%{_libdir}/samba/ldb/ldap.so
%{_libdir}/samba/libldb-cmdline-private-samba.so
%{_includedir}/samba-4.0/ldb_module.h
%{_includedir}/samba-4.0/ldb_handlers.h
%{_includedir}/samba-4.0/ldb_errors.h
%{_includedir}/samba-4.0/ldb_version.h
%{_includedir}/samba-4.0/ldb.h

%files -n python-ldb
%{python3_sitearch}/_ldb_text.py
%{python3_sitearch}/ldb.cpython-*.so
%{_libdir}/samba/libpyldb-util.cpython-*-private-samba.so

%if %{with ceph}
%files cephfs
%{_libdir}/samba/vfs/ceph.so
%{_libdir}/samba/vfs/ceph_new.so
%{_libdir}/samba/vfs/ceph_snapshots.so
%endif

%changelog
%autochangelog
