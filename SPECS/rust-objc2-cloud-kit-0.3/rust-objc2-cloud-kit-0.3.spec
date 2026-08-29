# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-cloud-kit
%global full_version 0.3.2
%global pkgname objc2-cloud-kit-0.3

Name:           rust-objc2-cloud-kit-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-cloud-kit"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:73ad74d880bb43877038da939b7427bba67e9dd42004a18b809ba7d87cee241c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.2
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/ckdefines) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}

%description
Source code for takopackized Rust crate "objc2-cloud-kit"

%package     -n %{name}+ckacceptsharesoperation
Summary:        Bindings to the CloudKit framework - feature "CKAcceptSharesOperation" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Provides:       crate(%{pkgname}/ckacceptsharesoperation) = %{version}
Provides:       crate(%{pkgname}/ckdiscoveruseridentitiesoperation) = %{version}
Provides:       crate(%{pkgname}/ckfetchshareparticipantsoperation) = %{version}
Provides:       crate(%{pkgname}/ckmodifyrecordzonesoperation) = %{version}

%description -n %{name}+ckacceptsharesoperation
This metapackage enables feature "CKAcceptSharesOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKDiscoverUserIdentitiesOperation", "CKFetchShareParticipantsOperation", and "CKModifyRecordZonesOperation" features.

%package     -n %{name}+ckallowedsharingoptions
Summary:        Bindings to the CloudKit framework - feature "CKAllowedSharingOptions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/ckallowedsharingoptions) = %{version}

%description -n %{name}+ckallowedsharingoptions
This metapackage enables feature "CKAllowedSharingOptions" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckasset
Summary:        Bindings to the CloudKit framework - feature "CKAsset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/ckasset) = %{version}

%description -n %{name}+ckasset
This metapackage enables feature "CKAsset" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckcontainer
Summary:        Bindings to the CloudKit framework - feature "CKContainer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/ckcontainer) = %{version}

%description -n %{name}+ckcontainer
This metapackage enables feature "CKContainer" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckdatabase
Summary:        Bindings to the CloudKit framework - feature "CKDatabase" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckdatabase) = %{version}
Provides:       crate(%{pkgname}/ckmodifysubscriptionsoperation) = %{version}

%description -n %{name}+ckdatabase
This metapackage enables feature "CKDatabase" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKModifySubscriptionsOperation" feature.

%package     -n %{name}+ckdatabaseoperation
Summary:        Bindings to the CloudKit framework - feature "CKDatabaseOperation" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Provides:       crate(%{pkgname}/ckdatabaseoperation) = %{version}
Provides:       crate(%{pkgname}/ckfetchnotificationchangesoperation) = %{version}
Provides:       crate(%{pkgname}/ckmarknotificationsreadoperation) = %{version}
Provides:       crate(%{pkgname}/ckmodifybadgeoperation) = %{version}

%description -n %{name}+ckdatabaseoperation
This metapackage enables feature "CKDatabaseOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKFetchNotificationChangesOperation", "CKMarkNotificationsReadOperation", and "CKModifyBadgeOperation" features.

%package     -n %{name}+ckdiscoveralluseridentitiesoperation
Summary:        Bindings to the CloudKit framework - feature "CKDiscoverAllUserIdentitiesOperation" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Provides:       crate(%{pkgname}/ckdiscoveralluseridentitiesoperation) = %{version}
Provides:       crate(%{pkgname}/ckfetchdatabasechangesoperation) = %{version}

%description -n %{name}+ckdiscoveralluseridentitiesoperation
This metapackage enables feature "CKDiscoverAllUserIdentitiesOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKFetchDatabaseChangesOperation" feature.

%package     -n %{name}+ckerror
Summary:        Bindings to the CloudKit framework - feature "CKError" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckerror) = %{version}
Provides:       crate(%{pkgname}/cksyncengineconfiguration) = %{version}

%description -n %{name}+ckerror
This metapackage enables feature "CKError" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKSyncEngineConfiguration" feature.

%package     -n %{name}+ckfetchrecordchangesoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchRecordChangesOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckfetchrecordchangesoperation) = %{version}

%description -n %{name}+ckfetchrecordchangesoperation
This metapackage enables feature "CKFetchRecordChangesOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckfetchrecordzonechangesoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchRecordZoneChangesOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckfetchrecordzonechangesoperation) = %{version}

%description -n %{name}+ckfetchrecordzonechangesoperation
This metapackage enables feature "CKFetchRecordZoneChangesOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckfetchrecordzonesoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchRecordZonesOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Provides:       crate(%{pkgname}/ckfetchrecordzonesoperation) = %{version}

%description -n %{name}+ckfetchrecordzonesoperation
This metapackage enables feature "CKFetchRecordZonesOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckfetchrecordsoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchRecordsOperation" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckfetchrecordsoperation) = %{version}
Provides:       crate(%{pkgname}/ckfetchsubscriptionsoperation) = %{version}

%description -n %{name}+ckfetchrecordsoperation
This metapackage enables feature "CKFetchRecordsOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKFetchSubscriptionsOperation" feature.

%package     -n %{name}+ckfetchsharemetadataoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchShareMetadataOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/ckfetchsharemetadataoperation) = %{version}

%description -n %{name}+ckfetchsharemetadataoperation
This metapackage enables feature "CKFetchShareMetadataOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckfetchwebauthtokenoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchWebAuthTokenOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckfetchwebauthtokenoperation) = %{version}

%description -n %{name}+ckfetchwebauthtokenoperation
This metapackage enables feature "CKFetchWebAuthTokenOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cklocationsortdescriptor
Summary:        Bindings to the CloudKit framework - feature "CKLocationSortDescriptor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/block2) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nssortdescriptor) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cklocationsortdescriptor) = %{version}

%description -n %{name}+cklocationsortdescriptor
This metapackage enables feature "CKLocationSortDescriptor" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckmodifyrecordsoperation
Summary:        Bindings to the CloudKit framework - feature "CKModifyRecordsOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Provides:       crate(%{pkgname}/ckmodifyrecordsoperation) = %{version}

%description -n %{name}+ckmodifyrecordsoperation
This metapackage enables feature "CKModifyRecordsOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cknotification
Summary:        Bindings to the CloudKit framework - feature "CKNotification"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/cknotification) = %{version}

%description -n %{name}+cknotification
This metapackage enables feature "CKNotification" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckoperation
Summary:        Bindings to the CloudKit framework - feature "CKOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckoperation) = %{version}

%description -n %{name}+ckoperation
This metapackage enables feature "CKOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckoperationgroup
Summary:        Bindings to the CloudKit framework - feature "CKOperationGroup"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckoperationgroup) = %{version}

%description -n %{name}+ckoperationgroup
This metapackage enables feature "CKOperationGroup" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckquery
Summary:        Bindings to the CloudKit framework - feature "CKQuery"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspredicate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nssortdescriptor) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckquery) = %{version}

%description -n %{name}+ckquery
This metapackage enables feature "CKQuery" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckqueryoperation
Summary:        Bindings to the CloudKit framework - feature "CKQueryOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckqueryoperation) = %{version}

%description -n %{name}+ckqueryoperation
This metapackage enables feature "CKQueryOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckrecord
Summary:        Bindings to the CloudKit framework - feature "CKRecord"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/ckrecord) = %{version}

%description -n %{name}+ckrecord
This metapackage enables feature "CKRecord" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckrecordid
Summary:        Bindings to the CloudKit framework - feature "CKRecordID" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckrecordid) = %{version}
Provides:       crate(%{pkgname}/ckrecordzoneid) = %{version}
Provides:       crate(%{pkgname}/cksharemetadata) = %{version}

%description -n %{name}+ckrecordid
This metapackage enables feature "CKRecordID" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKRecordZoneID", and "CKShareMetadata" features.

%package     -n %{name}+ckrecordzone
Summary:        Bindings to the CloudKit framework - feature "CKRecordZone"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckrecordzone) = %{version}

%description -n %{name}+ckrecordzone
This metapackage enables feature "CKRecordZone" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckreference
Summary:        Bindings to the CloudKit framework - feature "CKReference" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/ckreference) = %{version}
Provides:       crate(%{pkgname}/ckserverchangetoken) = %{version}
Provides:       crate(%{pkgname}/ckshareaccessrequester) = %{version}
Provides:       crate(%{pkgname}/ckshareblockedidentity) = %{version}

%description -n %{name}+ckreference
This metapackage enables feature "CKReference" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKServerChangeToken", "CKShareAccessRequester", and "CKShareBlockedIdentity" features.

%package     -n %{name}+ckshare
Summary:        Bindings to the CloudKit framework - feature "CKShare"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/ckshare) = %{version}

%description -n %{name}+ckshare
This metapackage enables feature "CKShare" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckshareparticipant
Summary:        Bindings to the CloudKit framework - feature "CKShareParticipant"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckshareparticipant) = %{version}

%description -n %{name}+ckshareparticipant
This metapackage enables feature "CKShareParticipant" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksharerequestaccessoperation
Summary:        Bindings to the CloudKit framework - feature "CKShareRequestAccessOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/cksharerequestaccessoperation) = %{version}

%description -n %{name}+cksharerequestaccessoperation
This metapackage enables feature "CKShareRequestAccessOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksubscription
Summary:        Bindings to the CloudKit framework - feature "CKSubscription"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspredicate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cksubscription) = %{version}

%description -n %{name}+cksubscription
This metapackage enables feature "CKSubscription" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksyncengine
Summary:        Bindings to the CloudKit framework - feature "CKSyncEngine"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/cksyncengine) = %{version}

%description -n %{name}+cksyncengine
This metapackage enables feature "CKSyncEngine" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksyncengineevent
Summary:        Bindings to the CloudKit framework - feature "CKSyncEngineEvent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cksyncengineevent) = %{version}

%description -n %{name}+cksyncengineevent
This metapackage enables feature "CKSyncEngineEvent" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksyncenginerecordzonechangebatch
Summary:        Bindings to the CloudKit framework - feature "CKSyncEngineRecordZoneChangeBatch"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Provides:       crate(%{pkgname}/cksyncenginerecordzonechangebatch) = %{version}

%description -n %{name}+cksyncenginerecordzonechangebatch
This metapackage enables feature "CKSyncEngineRecordZoneChangeBatch" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksyncenginestate
Summary:        Bindings to the CloudKit framework - feature "CKSyncEngineState"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/cksyncenginestate) = %{version}

%description -n %{name}+cksyncenginestate
This metapackage enables feature "CKSyncEngineState" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksystemsharinguiobserver
Summary:        Bindings to the CloudKit framework - feature "CKSystemSharingUIObserver"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Provides:       crate(%{pkgname}/cksystemsharinguiobserver) = %{version}

%description -n %{name}+cksystemsharinguiobserver
This metapackage enables feature "CKSystemSharingUIObserver" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckuseridentity
Summary:        Bindings to the CloudKit framework - feature "CKUserIdentity"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspersonnamecomponents) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckuseridentity) = %{version}

%description -n %{name}+ckuseridentity
This metapackage enables feature "CKUserIdentity" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckuseridentitylookupinfo
Summary:        Bindings to the CloudKit framework - feature "CKUserIdentityLookupInfo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/ckuseridentitylookupinfo) = %{version}

%description -n %{name}+ckuseridentitylookupinfo
This metapackage enables feature "CKUserIdentityLookupInfo" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsitemprovider-cksharingsupport
Summary:        Bindings to the CloudKit framework - feature "NSItemProvider_CKSharingSupport"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Provides:       crate(%{pkgname}/nsitemprovider-cksharingsupport) = %{version}

%description -n %{name}+nsitemprovider-cksharingsupport
This metapackage enables feature "NSItemProvider_CKSharingSupport" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the CloudKit framework - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the CloudKit framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the CloudKit framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/ckacceptsharesoperation) = %{version}
Requires:       crate(%{pkgname}/ckallowedsharingoptions) = %{version}
Requires:       crate(%{pkgname}/ckasset) = %{version}
Requires:       crate(%{pkgname}/ckcontainer) = %{version}
Requires:       crate(%{pkgname}/ckdatabase) = %{version}
Requires:       crate(%{pkgname}/ckdatabaseoperation) = %{version}
Requires:       crate(%{pkgname}/ckdefines) = %{version}
Requires:       crate(%{pkgname}/ckdiscoveralluseridentitiesoperation) = %{version}
Requires:       crate(%{pkgname}/ckdiscoveruseridentitiesoperation) = %{version}
Requires:       crate(%{pkgname}/ckerror) = %{version}
Requires:       crate(%{pkgname}/ckfetchdatabasechangesoperation) = %{version}
Requires:       crate(%{pkgname}/ckfetchnotificationchangesoperation) = %{version}
Requires:       crate(%{pkgname}/ckfetchrecordchangesoperation) = %{version}
Requires:       crate(%{pkgname}/ckfetchrecordsoperation) = %{version}
Requires:       crate(%{pkgname}/ckfetchrecordzonechangesoperation) = %{version}
Requires:       crate(%{pkgname}/ckfetchrecordzonesoperation) = %{version}
Requires:       crate(%{pkgname}/ckfetchsharemetadataoperation) = %{version}
Requires:       crate(%{pkgname}/ckfetchshareparticipantsoperation) = %{version}
Requires:       crate(%{pkgname}/ckfetchsubscriptionsoperation) = %{version}
Requires:       crate(%{pkgname}/ckfetchwebauthtokenoperation) = %{version}
Requires:       crate(%{pkgname}/cklocationsortdescriptor) = %{version}
Requires:       crate(%{pkgname}/ckmarknotificationsreadoperation) = %{version}
Requires:       crate(%{pkgname}/ckmodifybadgeoperation) = %{version}
Requires:       crate(%{pkgname}/ckmodifyrecordsoperation) = %{version}
Requires:       crate(%{pkgname}/ckmodifyrecordzonesoperation) = %{version}
Requires:       crate(%{pkgname}/ckmodifysubscriptionsoperation) = %{version}
Requires:       crate(%{pkgname}/cknotification) = %{version}
Requires:       crate(%{pkgname}/ckoperation) = %{version}
Requires:       crate(%{pkgname}/ckoperationgroup) = %{version}
Requires:       crate(%{pkgname}/ckquery) = %{version}
Requires:       crate(%{pkgname}/ckqueryoperation) = %{version}
Requires:       crate(%{pkgname}/ckrecord) = %{version}
Requires:       crate(%{pkgname}/ckrecordid) = %{version}
Requires:       crate(%{pkgname}/ckrecordzone) = %{version}
Requires:       crate(%{pkgname}/ckrecordzoneid) = %{version}
Requires:       crate(%{pkgname}/ckreference) = %{version}
Requires:       crate(%{pkgname}/ckserverchangetoken) = %{version}
Requires:       crate(%{pkgname}/ckshare) = %{version}
Requires:       crate(%{pkgname}/ckshareaccessrequester) = %{version}
Requires:       crate(%{pkgname}/ckshareblockedidentity) = %{version}
Requires:       crate(%{pkgname}/cksharemetadata) = %{version}
Requires:       crate(%{pkgname}/ckshareparticipant) = %{version}
Requires:       crate(%{pkgname}/cksharerequestaccessoperation) = %{version}
Requires:       crate(%{pkgname}/cksubscription) = %{version}
Requires:       crate(%{pkgname}/cksyncengine) = %{version}
Requires:       crate(%{pkgname}/cksyncengineconfiguration) = %{version}
Requires:       crate(%{pkgname}/cksyncengineevent) = %{version}
Requires:       crate(%{pkgname}/cksyncenginerecordzonechangebatch) = %{version}
Requires:       crate(%{pkgname}/cksyncenginestate) = %{version}
Requires:       crate(%{pkgname}/cksystemsharinguiobserver) = %{version}
Requires:       crate(%{pkgname}/ckuseridentity) = %{version}
Requires:       crate(%{pkgname}/ckuseridentitylookupinfo) = %{version}
Requires:       crate(%{pkgname}/nsitemprovider-cksharingsupport) = %{version}
Requires:       crate(%{pkgname}/objc2-contacts) = %{version}
Requires:       crate(%{pkgname}/objc2-core-location) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-contacts
Summary:        Bindings to the CloudKit framework - feature "objc2-contacts"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-contacts-0.3/cncontact) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-contacts) = %{version}

%description -n %{name}+objc2-contacts
This metapackage enables feature "objc2-contacts" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-location
Summary:        Bindings to the CloudKit framework - feature "objc2-core-location"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-location-0.3/cllocation) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-location) = %{version}

%description -n %{name}+objc2-core-location
This metapackage enables feature "objc2-core-location" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
