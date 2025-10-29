# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define run_test_suite 0
%define slapdrundir %{_rundir}/slapd

%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

Name:           openldap
Version:        2.6.10
Release:        %autorelease
Summary:        An implementation of the Lightweight Directory Access Protocol
License:        OLDAP-2.8
URL:            https://www.openldap.org
#!RemoteAsset
Source0:        https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-%{version}.tgz
#!RemoteAsset
Source1:        https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-%{version}.tgz.asc
Source2:        slapd.conf
Source3:        sasl-slapd.conf
Source4:        README.module-loading
Source5:        schema2ldif
Source6:        slapd.conf.olctemplate
Source7:        slapd.conf.example
Source8:        start
Source9:        slapd.service
Source10:       sysconfig.openldap
Source11:       openldap.conf
Source12:       ldap-user.conf
Source13:       fixup-modulepath.sh
Source14:       slapd-ldif-update-crc.sh
Source15:       update-crc.sh

Patch0:         0001-reproducible.patch
Patch1:         0002-LDAPI-socket-location.patch
Patch2:         0003-pie-compile.patch
Patch3:         0004-In-monitor-backend-do-not-return-Connection0-entries.patch
Patch4:         0005-Clear-shared-key-only-in-close-function.patch
Patch5:         0006-gcc14-v2.patch
BuildSystem:    autotools

BuildOption(conf): --sysconfdir=%{_sysconfdir}/openldap
BuildOption(conf): --libexecdir=%{_libexecdir}
BuildOption(conf): --localstatedir=%{slapdrundir}
BuildOption(conf): --enable-wrappers=no
BuildOption(conf): --enable-spasswd
BuildOption(conf): --enable-modules
BuildOption(conf): --enable-shared
BuildOption(conf): --enable-dynamic
BuildOption(conf): --with-tls=openssl
BuildOption(conf): --with-cyrus-sasl
BuildOption(conf): --enable-crypt
BuildOption(conf): --enable-ipv6=yes
BuildOption(conf): --enable-dynacl
BuildOption(conf): --enable-aci
BuildOption(conf): --enable-ldap=mod
BuildOption(conf): --enable-meta=mod
BuildOption(conf): --enable-perl=mod
BuildOption(conf): --enable-sock=mod
BuildOption(conf): --enable-sql=mod
BuildOption(conf): --enable-mdb=mod
BuildOption(conf): --enable-relay=mod
BuildOption(conf): --enable-overlays=mod
BuildOption(conf): --enable-syncprov=mod
BuildOption(conf): --enable-ppolicy=mod
BuildOption(conf): --with-yielding-select
BuildOption(conf): --with-argon2=libargon2

BuildOption(install): STRIP="" "sysconfdir=%{_sysconfdir}/openldap" "libexecdir=%{_libexecdir}"

BuildRequires:  libargon2-devel cyrus-sasl-devel db-devel mandoc libtool sysuser-tools unixODBC-devel
BuildRequires:  pkgconfig(krb5) pkgconfig(systemd) pkgconfig(openssl)
Requires:       /usr/bin/awk
Requires:       libldap2 = %{version}
Recommends:     cyrus-sasl
%sysusers_requires

%description
OpenLDAP is a client and server reference implementation of the
Lightweight Directory Access Protocol v3 (LDAPv3).

The server provides several database backends and overlays.

%package        back-perl
Summary:        OpenLDAP Perl backend
Requires:       %{name} = %{version}
Requires:       perl

%description    back-perl
The OpenLDAP Perl back-end allows you to execute Perl code specific to
different LDAP operations.

%package        back-sock
Summary:        OpenLDAP Socket backend
Requires:       %{name} = %{version}
Provides:       %{name}:/usr/share/man/man5/slapd-sock.5.gz

%description    back-sock
The OpenLDAP socket back-end allows you to handle LDAP requests and
results with an external process listening on a Unix domain socket.

%package        back-meta
Summary:        OpenLDAP Meta backend
Requires:       %{name} = %{version}
Provides:       %{name}:/usr/share/man/man5/slapd-meta.5.gz

%description    back-meta
The OpenLDAP Meta back-end is able to perform basic LDAP proxying with
respect to a set of remote LDAP servers. The information contained in
these servers can be presented as belonging to a single Directory
Information Tree (DIT).

%package        back-sql
Summary:        OpenLDAP SQL backend
Requires:       %{name} = %{version}

%description    back-sql
The primary purpose of this OpenLDAP backend is to present information
stored in a Relational (SQL) Database as an LDAP subtree without the need
to do any programming.

%package -n     libldap-data
Summary:        Configuration file for system-wide defaults for all uses of libldap
BuildArch:      noarch

%description -n libldap-data
The subpackage contains a configuration file used to set system-wide defaults
to be applied with all usages of libldap.

%package        contrib
Summary:        OpenLDAP Contrib Modules
Requires:       %{name} = %{version}

%description    contrib
Various overlays found in contrib/:
addpartial    Intercepts ADD requests, applies changes to existing entries
allop
allowed       Generates attributes indicating access rights
autogroup
authzid       implements RFC 3829 support
cloak
datamorph     store enumerated values and fixed size integers
denyop
lastbind      writes last bind timestamp to entry
noopsrch      handles no-op search control
pw-sha2       generates/validates SHA-2 password hashes
pw-pbkdf2     generates/validates PBKDF2 password hashes
smbk5pwd      generates Samba3 password hashes (heimdal krb disabled)
trace         traces overlay invocation
variant       allows attributes/values to be shared between several entries
vc            implements the verify credentials extended operation

%package        client
Summary:        OpenLDAP client utilities
Requires:       libldap2 = %{version}

%description    client
OpenLDAP client utilities such as ldapadd, ldapsearch, ldapmodify.

%package        devel
Summary:        Libraries, Header Files and Documentation for OpenLDAP
Conflicts:      openldap-devel
Requires:       libldap2 = %{version}
Recommends:     cyrus-sasl-devel

%description    devel
This package provides the OpenLDAP libraries, header files, and
documentation.

%package        static
Summary:        Static libraries for the OpenLDAP libraries
Requires:       cyrus-sasl-devel
Requires:       openssl-devel
Requires:       %{name}-devel = %version

%description    static
This package provides the static versions of the OpenLDAP libraries
for development.

%package -n     libldap2
Summary:        OpenLDAP Client Libraries
Recommends:     libldap-data >= %{version}

%description -n libldap2
This package contains the OpenLDAP client libraries.

%package -n     libldapcpp-devel
Summary:        C++ wrapper around openLDAP API
Requires:       libldapcpp0 = %{version}
Requires:       %{name}-devel

%description -n libldapcpp-devel
This package contains files needed for development with the LDAP C++
library.

%package -n     libldapcpp0
Summary:        C++ wrapper around openLDAP API
Provides:       ldapcpplib = %{version}
Obsoletes:      ldapcpplib <= 0.0.5

%description -n libldapcpp0
This package provides a C++ library for accessing LDAP (Version 3)
Servers

%build -p
cp %{SOURCE4} .
make depend
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags} -Wno-format-extra-args -fno-strict-aliasing -DNDEBUG -DSLAP_CONFIG_DELETE -DSLAP_SCHEMA_EXPOSE -DLDAP_COLLECTIVE_ATTRIBUTES -DLDAP_USE_NON_BLOCKING_TLS"
export STRIP=""

%build -a
# Build selected contrib overlays
for SLAPO_NAME in addpartial allowed allop autogroup authzid datamorph lastbind denyop cloak noopsrch passwd/sha2 passwd/pbkdf2 trace variant vc
do
  make -C contrib/slapd-modules/${SLAPO_NAME} %{?_smp_mflags} "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libexecdir}"
done
# slapo-smbk5pwd only for Samba password hashes
make -C contrib/slapd-modules/smbk5pwd %{?_smp_mflags} "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libexecdir}" DEFS="-DDO_SAMBA" HEIMDAL_LIB=""

%check
%if %run_test_suite
# calculate the base port to be use in the test-suite
SLAPD_BASEPORT=10000
if [ -f /.buildenv ] ; then
    . /.buildenv
    SLAPD_BASEPORT=$(($SLAPD_BASEPORT + ${BUILD_INCARNATION:-0} * 10))
fi
export SLAPD_BASEPORT
rm -f tests/scripts/test019-syncreplication-cascade
rm -f tests/scripts/test022-ppolicy
rm -f tests/scripts/test023-refint
rm -f tests/scripts/test033-glue-syncrepl
#rm -f tests/scripts/test036-meta-concurrency
#rm -f tests/scripts/test039-glue-ldap-concurrency
rm -f tests/scripts/test043-delta-syncrepl
#rm -f tests/scripts/test045-syncreplication-proxied
rm -f tests/scripts/test048-syncrepl-multiproxy
rm -f tests/scripts/test050-syncrepl-multimaster
rm -f tests/scripts/test058-syncrepl-asymmetric
make SLAPD_DEBUG=0 test
%endif

%install
mkdir -p %{buildroot}%{_libdir}/openldap
mkdir -p %{buildroot}/usr/lib/openldap
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
make STRIP="" DESTDIR="%{buildroot}" "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libexecdir}" install

# Additional symbolic link to slapd executable in /usr/sbin/
rm -f %{buildroot}%{_sbindir}/slapd
(cd %{buildroot}%{_sbindir} && ln -s ../lib64/slapd slapd)

# Install selected contrib overlays
for SLAPO_NAME in addpartial allowed allop autogroup authzid datamorph lastbind denyop cloak noopsrch passwd/sha2 passwd/pbkdf2 trace variant vc
do
  make -C contrib/slapd-modules/${SLAPO_NAME} STRIP="" DESTDIR="%{buildroot}" "mandir=%{_mandir}" "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libexecdir}" install
done
# slapo-smbk5pwd only for Samba password hashes
make -C contrib/slapd-modules/smbk5pwd STRIP="" DESTDIR="%{buildroot}" "mandir=%{_mandir}" "sysconfdir=%{_sysconfdir}/openldap" "libdir=%{_libdir}" "libexecdir=%{_libexecdir}" install
install -m 755 %{SOURCE8} %{buildroot}/usr/lib/openldap/start
install -m 644 %{SOURCE9} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/openldap/slapd.d
mkdir -p %{buildroot}%{_sysconfdir}/sasl2
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sasl2/slapd.conf
install -m 755 -d %{buildroot}/var/lib/ldap
chmod a+x %{buildroot}%{_libdir}/liblber.so*
chmod a+x %{buildroot}%{_libdir}/libldap.so*
install -m 755 %{SOURCE5} %{buildroot}%{_sbindir}/schema2ldif
mkdir -p  %{buildroot}%{_tmpfilesdir}/
install -m 644 %{SOURCE11} %{buildroot}%{_tmpfilesdir}/
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE12} %{buildroot}%{_sysusersdir}/

install -m 755 %{SOURCE12}  ${RPM_BUILD_ROOT}/usr/lib/openldap/fixup-modulepath
install -m 755 %{SOURCE13}  ${RPM_BUILD_ROOT}/%{_sbindir}/slapd-ldif-update-crc
install -m 755 %{SOURCE14}  ${RPM_BUILD_ROOT}/usr/lib/openldap/update-crc

mkdir -p %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE10} %{buildroot}%{_fillupdir}/sysconfig.openldap
# Install default and sample configuration files
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/openldap
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/openldap
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/openldap
find doc/guide '(' ! -name *.html -a ! -name *.gif -a ! -name *.png -a ! -type d ')' -delete
rm -rf doc/guide/release

%define DOCDIR %{_defaultdocdir}/%{name}
# Install default database optimisation
install -d %{buildroot}%{DOCDIR}/adminguide \
           %{buildroot}%{DOCDIR}/images \
           %{buildroot}%{DOCDIR}/drafts
install -m 644 doc/guide/admin/* %{buildroot}%{DOCDIR}/adminguide
install -m 644 doc/guide/images/*.gif %{buildroot}%{DOCDIR}/images
install -m 644 doc/drafts/* %{buildroot}%{DOCDIR}/drafts
install -m 644 ANNOUNCEMENT \
               COPYRIGHT \
               README \
               CHANGES \
               %{SOURCE4} \
               %{buildroot}%{DOCDIR}
install -m 644 servers/slapd/slapd.ldif \
               %{buildroot}%{DOCDIR}/slapd.ldif.default
rm -f %{buildroot}/etc/openldap/schema/README
rm -f %{buildroot}/etc/openldap/slapd.ldif*
mv servers/slapd/back-sql/rdbms_depend servers/slapd/back-sql/examples

rm -f %{buildroot}%{_libdir}/openldap/*.a
rm -f %{buildroot}/usr/share/man/man5/slapd-dnssrv.5
rm -f %{buildroot}/usr/share/man/man5/slapd-null.5
rm -f %{buildroot}/usr/share/man/man5/slapd-passwd.5
rm -f %{buildroot}/usr/share/man/man5/slapd-shell.5
rm -f %{buildroot}/usr/share/man/man5/slapd-tcl.5
# Remove *.la files, libtool does not handle this correct
# Keep .la files for modules in the openldap subdirectory, which are consumed
# in this form.
rm -f  %{buildroot}%{_libdir}/*.la

# Provide a libldap_r for backwards-compatibility with OpenLDAP < 2.5.
ln -fs libldap.so "%{buildroot}%{_libdir}/libldap_r.so"

%pre
%sysusers_create_package ldap-user.conf %SOURCE12
%tmpfiles_create_package %{name} %SOURCE11

%post
%systemd_post slapd.service

%ldconfig_scriptlets -n libldap2

%preun
%systemd_preun slapd.service

%postun
%systemd_postun slapd.service

%files
%config %{_sysconfdir}/openldap/schema/*.schema
%config %{_sysconfdir}/openldap/schema/*.ldif
%config(noreplace) /etc/sasl2/slapd.conf
%config(noreplace) %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf
%config(noreplace) %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf.olctemplate
%config %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf.default
%config %attr(640, root, ldap) %{_sysconfdir}/openldap/slapd.conf.example
%dir /usr/lib/openldap
%dir %{_sysconfdir}/sasl2
%dir %{_sysconfdir}/openldap
%dir %attr(0770, ldap, ldap) %{_sysconfdir}/openldap/slapd.d
%dir %{_sysconfdir}/openldap/schema
%{_fillupdir}/sysconfig.openldap
%{_sbindir}/slap*
%{_libexecdir}/openldap/*
%exclude %{_libexecdir}/openldap/back_meta*
%exclude %{_libexecdir}/openldap/back_sql*
%exclude %{_libexecdir}/openldap/back_perl*
%exclude %{_libexecdir}/openldap/back_sock*
%{_libexecdir}/slapd
/usr/lib/openldap/*
%{_unitdir}/slapd.service
%{_tmpfilesdir}/openldap.conf
%{_sysusersdir}/ldap-user.conf
%dir %attr(0750, ldap, ldap) %{_sharedstatedir}/ldap
%ghost %attr(0750, ldap, ldap) %{slapdrundir}
%doc %{_mandir}/man8/sl*
%doc %{_mandir}/man8/lloadd.*
%doc %{_mandir}/man5/*
%dir %{DOCDIR}
%doc %{DOCDIR}/ANNOUNCEMENT
%doc %{DOCDIR}/COPYRIGHT
%license LICENSE
%doc %{DOCDIR}/README*
%doc %{DOCDIR}/CHANGES
%doc %{DOCDIR}/slapd.ldif.default
%doc %{DOCDIR}/drafts
%doc %{DOCDIR}/adminguide
%doc %{DOCDIR}/images
%{_libdir}/liblber.so.*
%{_libdir}/libldap.so.*

%files back-perl
%{_libexecdir}/openldap/back_perl*
%doc %{_mandir}/man5/slapd-perl.*

%files back-sock
%{_libexecdir}/openldap/back_sock*
%doc %{_mandir}/man5/slapd-sock.*

%files back-meta
%{_libexecdir}/openldap/back_meta*
%doc %{_mandir}/man5/slapd-meta.*

%files back-sql
%{_libexecdir}/openldap/back_sql*
%doc %{_mandir}/man5/slapd-sql.*
%doc servers/slapd/back-sql/examples
%doc servers/slapd/back-sql/docs/bugs
%doc servers/slapd/back-sql/docs/install

%files -n libldap-data
%config(noreplace) %{_sysconfdir}/openldap/ldap.conf
%doc %{_mandir}/man5/ldap.conf*
%{_sysconfdir}/openldap/ldap.conf.default

%files contrib
%{_libexecdir}/openldap/addpartial.*
%{_libexecdir}/openldap/allop.*
%{_libexecdir}/openldap/allowed.*
%{_libexecdir}/openldap/authzid.*
%{_libexecdir}/openldap/autogroup.*
%{_libexecdir}/openldap/cloak.*
%{_libexecdir}/openldap/datamorph.*
%{_libexecdir}/openldap/denyop.*
%{_libexecdir}/openldap/lastbind.*
%{_libexecdir}/openldap/noopsrch.*
%{_libexecdir}/openldap/pw-pbkdf2.*
%{_libexecdir}/openldap/pw-sha2.*
%{_libexecdir}/openldap/smbk5pwd.*
%{_libexecdir}/openldap/trace.*
%{_libexecdir}/openldap/variant.*
%{_libexecdir}/openldap/vc.*

%files client
%doc %{_mandir}/man1/ldap*
%doc %{_mandir}/man5/ldif.*
%dir /etc/openldap
%{_sbindir}/schema2ldif
%{_bindir}/ldap*

%files devel
%doc %{_mandir}/man3/*
%{_includedir}/*.h
%{_libdir}/liblber.so
%{_libdir}/libldap*.so
%{_libdir}/pkgconfig/*.pc

%files static
%_libdir/liblber.a
%_libdir/libldap*.a

%files -n libldap2
%{_libdir}/liblber.so.*
%{_libdir}/libldap.so.*

%changelog
%{?autochangelog}
