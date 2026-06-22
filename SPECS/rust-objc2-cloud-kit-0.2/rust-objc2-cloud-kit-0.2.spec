# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-cloud-kit
%global full_version 0.2.2
%global pkgname objc2-cloud-kit-0.2

Name:           rust-objc2-cloud-kit-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-cloud-kit"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:74dd3b56391c7a0596a295029734d3c1c5e7e510a4cb30245f8221ccea96b009
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/ckdefines) = %{version}

%description
Source code for takopackized Rust crate "objc2-cloud-kit"

%package     -n %{name}+ckacceptsharesoperation
Summary:        Bindings to the CloudKit framework - feature "CKAcceptSharesOperation" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Provides:       crate(%{pkgname}/ckacceptsharesoperation) = %{version}
Provides:       crate(%{pkgname}/ckdiscoveruseridentitiesoperation) = %{version}
Provides:       crate(%{pkgname}/ckfetchshareparticipantsoperation) = %{version}
Provides:       crate(%{pkgname}/ckmarknotificationsreadoperation) = %{version}
Provides:       crate(%{pkgname}/ckmodifyrecordzonesoperation) = %{version}

%description -n %{name}+ckacceptsharesoperation
This metapackage enables feature "CKAcceptSharesOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKDiscoverUserIdentitiesOperation", "CKFetchShareParticipantsOperation", "CKMarkNotificationsReadOperation", and "CKModifyRecordZonesOperation" features.

%package     -n %{name}+ckallowedsharingoptions
Summary:        Bindings to the CloudKit framework - feature "CKAllowedSharingOptions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/ckallowedsharingoptions) = %{version}

%description -n %{name}+ckallowedsharingoptions
This metapackage enables feature "CKAllowedSharingOptions" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckasset
Summary:        Bindings to the CloudKit framework - feature "CKAsset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/ckasset) = %{version}

%description -n %{name}+ckasset
This metapackage enables feature "CKAsset" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckcontainer
Summary:        Bindings to the CloudKit framework - feature "CKContainer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/ckcontainer) = %{version}

%description -n %{name}+ckcontainer
This metapackage enables feature "CKContainer" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckdatabase
Summary:        Bindings to the CloudKit framework - feature "CKDatabase" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckdatabase) = %{version}
Provides:       crate(%{pkgname}/ckmodifysubscriptionsoperation) = %{version}

%description -n %{name}+ckdatabase
This metapackage enables feature "CKDatabase" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKModifySubscriptionsOperation" feature.

%package     -n %{name}+ckdatabaseoperation
Summary:        Bindings to the CloudKit framework - feature "CKDatabaseOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Provides:       crate(%{pkgname}/ckdatabaseoperation) = %{version}

%description -n %{name}+ckdatabaseoperation
This metapackage enables feature "CKDatabaseOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckdiscoveralluseridentitiesoperation
Summary:        Bindings to the CloudKit framework - feature "CKDiscoverAllUserIdentitiesOperation" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Provides:       crate(%{pkgname}/ckdiscoveralluseridentitiesoperation) = %{version}
Provides:       crate(%{pkgname}/ckfetchdatabasechangesoperation) = %{version}
Provides:       crate(%{pkgname}/ckfetchnotificationchangesoperation) = %{version}
Provides:       crate(%{pkgname}/ckmodifybadgeoperation) = %{version}

%description -n %{name}+ckdiscoveralluseridentitiesoperation
This metapackage enables feature "CKDiscoverAllUserIdentitiesOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKFetchDatabaseChangesOperation", "CKFetchNotificationChangesOperation", and "CKModifyBadgeOperation" features.

%package     -n %{name}+ckerror
Summary:        Bindings to the CloudKit framework - feature "CKError" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckerror) = %{version}
Provides:       crate(%{pkgname}/cksyncengineconfiguration) = %{version}

%description -n %{name}+ckerror
This metapackage enables feature "CKError" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKSyncEngineConfiguration" feature.

%package     -n %{name}+ckfetchrecordchangesoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchRecordChangesOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckfetchrecordchangesoperation) = %{version}

%description -n %{name}+ckfetchrecordchangesoperation
This metapackage enables feature "CKFetchRecordChangesOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckfetchrecordzonechangesoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchRecordZoneChangesOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckfetchrecordzonechangesoperation) = %{version}

%description -n %{name}+ckfetchrecordzonechangesoperation
This metapackage enables feature "CKFetchRecordZoneChangesOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckfetchrecordzonesoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchRecordZonesOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Provides:       crate(%{pkgname}/ckfetchrecordzonesoperation) = %{version}

%description -n %{name}+ckfetchrecordzonesoperation
This metapackage enables feature "CKFetchRecordZonesOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckfetchrecordsoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchRecordsOperation" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckfetchrecordsoperation) = %{version}
Provides:       crate(%{pkgname}/ckfetchsubscriptionsoperation) = %{version}

%description -n %{name}+ckfetchrecordsoperation
This metapackage enables feature "CKFetchRecordsOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKFetchSubscriptionsOperation" feature.

%package     -n %{name}+ckfetchsharemetadataoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchShareMetadataOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/ckfetchsharemetadataoperation) = %{version}

%description -n %{name}+ckfetchsharemetadataoperation
This metapackage enables feature "CKFetchShareMetadataOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckfetchwebauthtokenoperation
Summary:        Bindings to the CloudKit framework - feature "CKFetchWebAuthTokenOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckfetchwebauthtokenoperation) = %{version}

%description -n %{name}+ckfetchwebauthtokenoperation
This metapackage enables feature "CKFetchWebAuthTokenOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cklocationsortdescriptor
Summary:        Bindings to the CloudKit framework - feature "CKLocationSortDescriptor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-location-0.2/cllocation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nssortdescriptor) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cklocationsortdescriptor) = %{version}

%description -n %{name}+cklocationsortdescriptor
This metapackage enables feature "CKLocationSortDescriptor" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckmodifyrecordsoperation
Summary:        Bindings to the CloudKit framework - feature "CKModifyRecordsOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Provides:       crate(%{pkgname}/ckmodifyrecordsoperation) = %{version}

%description -n %{name}+ckmodifyrecordsoperation
This metapackage enables feature "CKModifyRecordsOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cknotification
Summary:        Bindings to the CloudKit framework - feature "CKNotification"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/cknotification) = %{version}

%description -n %{name}+cknotification
This metapackage enables feature "CKNotification" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckoperation
Summary:        Bindings to the CloudKit framework - feature "CKOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckoperation) = %{version}

%description -n %{name}+ckoperation
This metapackage enables feature "CKOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckoperationgroup
Summary:        Bindings to the CloudKit framework - feature "CKOperationGroup"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckoperationgroup) = %{version}

%description -n %{name}+ckoperationgroup
This metapackage enables feature "CKOperationGroup" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckquery
Summary:        Bindings to the CloudKit framework - feature "CKQuery"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nssortdescriptor) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckquery) = %{version}

%description -n %{name}+ckquery
This metapackage enables feature "CKQuery" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckqueryoperation
Summary:        Bindings to the CloudKit framework - feature "CKQueryOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckqueryoperation) = %{version}

%description -n %{name}+ckqueryoperation
This metapackage enables feature "CKQueryOperation" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckrecord
Summary:        Bindings to the CloudKit framework - feature "CKRecord"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-location-0.2/cllocation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/ckrecord) = %{version}

%description -n %{name}+ckrecord
This metapackage enables feature "CKRecord" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckrecordid
Summary:        Bindings to the CloudKit framework - feature "CKRecordID" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
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
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckrecordzone) = %{version}

%description -n %{name}+ckrecordzone
This metapackage enables feature "CKRecordZone" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckreference
Summary:        Bindings to the CloudKit framework - feature "CKReference" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/ckreference) = %{version}
Provides:       crate(%{pkgname}/ckserverchangetoken) = %{version}
Provides:       crate(%{pkgname}/ckshareparticipant) = %{version}

%description -n %{name}+ckreference
This metapackage enables feature "CKReference" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CKServerChangeToken", and "CKShareParticipant" features.

%package     -n %{name}+ckshare
Summary:        Bindings to the CloudKit framework - feature "CKShare"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/ckshare) = %{version}

%description -n %{name}+ckshare
This metapackage enables feature "CKShare" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksubscription
Summary:        Bindings to the CloudKit framework - feature "CKSubscription"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cksubscription) = %{version}

%description -n %{name}+cksubscription
This metapackage enables feature "CKSubscription" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksyncengine
Summary:        Bindings to the CloudKit framework - feature "CKSyncEngine"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Provides:       crate(%{pkgname}/cksyncengine) = %{version}

%description -n %{name}+cksyncengine
This metapackage enables feature "CKSyncEngine" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksyncengineevent
Summary:        Bindings to the CloudKit framework - feature "CKSyncEngineEvent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cksyncengineevent) = %{version}

%description -n %{name}+cksyncengineevent
This metapackage enables feature "CKSyncEngineEvent" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksyncenginerecordzonechangebatch
Summary:        Bindings to the CloudKit framework - feature "CKSyncEngineRecordZoneChangeBatch"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Provides:       crate(%{pkgname}/cksyncenginerecordzonechangebatch) = %{version}

%description -n %{name}+cksyncenginerecordzonechangebatch
This metapackage enables feature "CKSyncEngineRecordZoneChangeBatch" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksyncenginestate
Summary:        Bindings to the CloudKit framework - feature "CKSyncEngineState"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/cksyncenginestate) = %{version}

%description -n %{name}+cksyncenginestate
This metapackage enables feature "CKSyncEngineState" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cksystemsharinguiobserver
Summary:        Bindings to the CloudKit framework - feature "CKSystemSharingUIObserver"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Provides:       crate(%{pkgname}/cksystemsharinguiobserver) = %{version}

%description -n %{name}+cksystemsharinguiobserver
This metapackage enables feature "CKSystemSharingUIObserver" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckuseridentity
Summary:        Bindings to the CloudKit framework - feature "CKUserIdentity"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspersonnamecomponents) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckuseridentity) = %{version}

%description -n %{name}+ckuseridentity
This metapackage enables feature "CKUserIdentity" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ckuseridentitylookupinfo
Summary:        Bindings to the CloudKit framework - feature "CKUserIdentityLookupInfo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/ckuseridentitylookupinfo) = %{version}

%description -n %{name}+ckuseridentitylookupinfo
This metapackage enables feature "CKUserIdentityLookupInfo" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsitemprovider-cksharingsupport
Summary:        Bindings to the CloudKit framework - feature "NSItemProvider_CKSharingSupport"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsitemprovider) >= 0.2.2
Provides:       crate(%{pkgname}/nsitemprovider-cksharingsupport) = %{version}

%description -n %{name}+nsitemprovider-cksharingsupport
This metapackage enables feature "NSItemProvider_CKSharingSupport" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Bindings to the CloudKit framework - feature "all"
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
Requires:       crate(%{pkgname}/cksharemetadata) = %{version}
Requires:       crate(%{pkgname}/ckshareparticipant) = %{version}
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
Requires:       crate(%{pkgname}/objc2-core-location) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Bindings to the CloudKit framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/alloc) >= 0.5.1
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-core-location-0.2/alloc) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the CloudKit framework - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2) >= 2.5.0
Requires:       crate(objc2-foundation-0.2/bitflags) >= 0.2.2
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the CloudKit framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5) >= 0.5.1
Requires:       crate(objc2-core-location-0.2/block2) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-location
Summary:        Bindings to the CloudKit framework - feature "objc2-core-location"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-location-0.2) >= 0.2.2
Provides:       crate(%{pkgname}/objc2-core-location) = %{version}

%description -n %{name}+objc2-core-location
This metapackage enables feature "objc2-core-location" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the CloudKit framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Requires:       crate(block2-0.5/std) >= 0.5.1
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-core-location-0.2/std) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-cloud-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
